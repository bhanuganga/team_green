# Create your views here.
from datetime import date
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from models import Events, Cities, User


def login(request):
    email = request.POST.get('user_email')
    password = request.POST.get('user_password')
    try:
        user = User.objects.get(user_email=email, user_password=password)
        request.session['username'] = user.user_name
        return HttpResponse("add_event_html")
    except User.DoesNotExist:
        return HttpResponse("Please register!")


def register(request):
    register_name = request.POST.get('register_name')
    register_email = request.POST.get('register_email')
    register_phone = request.POST.get('register_phone')
    register_password = request.POST.get('register_password')

    try:
        user = User.objects.get(user_email=register_email)
        return HttpResponse("Already registered!<br> Please login")
    except:
        user_instance = User(register_name, register_email, register_phone, register_password)
        user_instance.save()
        return HttpResponse("Successfully registered!<br>Login now")


def logout(request):
    del request.session['username']
    return HttpResponseRedirect(reverse("eventsapp_home"))


# @app.route('/')
def home(request):
    try:
        user_is = request.session['username']
    except KeyError:
        user_is = "not signed in"
        request.session['username'] = user_is
    return render(request, 'layout.html', {'user_name': user_is})


# @app.route("/add_event_h")    #Render add_event html
def add_event_html(request):
    """Add Event HTML page."""
    user_is = request.session['username']
    return render(request, "add_event.html", {"data": Cities.objects.values("place"),
                                              'user_name': user_is})


# @app.route('/add', methods=["POST"])

def add(request):
    """Adding event functionality achieved through ajax call."""
    user_is = request.session['username']
    if user_is != "not signed in":
        data = Cities.objects.values("place")
        name = request.POST.get('name')
        date_is = request.POST.get('date')  # variable with name "date" is shadowing inbuilt date()
        city = request.POST.get('cities')
        if city:
            city = city.capitalize()
        if city == 'Other':
            city = request.POST.get('other_city').capitalize()
        info = request.POST.get('info')
        if city not in data:
            city_instance = Cities(place=city)
            city_instance.save()
        user_obj = User.objects.get(user_name=user_is)
        event_instance = Events(name=name, date=date_is, city_id=city, info=info, user_id=user_obj.user_email)
        event_instance.save()
        message = "Event added!"
    else:
        message = "Sign in to add events!"
    return HttpResponse(message)


# @app.route("/search_event_h")          #Render search_html

def search_modify_html(request):
    """Render the list of event names in ascending order of date."""
    try:
        user_is = request.session['username']
        user_obj = User.objects.get(user_name=user_is)
        return render(request, "search_modify.html",
                      {'events_list': Events.objects.filter(user=user_obj.user_email).order_by('date'),
                       'user_name': user_is})
    except User.DoesNotExist:
        return HttpResponseRedirect(reverse("eventsapp_home"))


# @app.route('/search', methods=['POST'])
def search(request):
    """Through ajax call: Search Event by id."""
    if request.method == 'POST':
        cities_list = Cities.objects.values()
        event_id = request.POST["event_is"]
        if event_id != "default":
            event_instance = Events.objects.get(id=event_id)
            event_instance.date = str(event_instance.date)
            return render(request, 'search_result.html', {'instance': event_instance, 'id': event_id,
                                                          'cities_list': cities_list})
        else:
            return HttpResponse("please select a name from the list!")


# @app.route("/update", methods=["POST"])

def update(request):
    """Through ajax call: Update an event by id , takes the field values as new values if not modified."""
    data = Cities.objects.values("place")
    upd_name = request.POST.get("upd_name")
    upd_date = request.POST.get("upd_date")
    upd_city = request.POST.get("upd_city")
    if upd_city:
        upd_city = upd_city.capitalize()
    upd_info = request.POST.get("upd_info")
    event_id = request.POST.get("id")
    event_obj = Events.objects.get(id=event_id)
    if upd_city not in data:
        city_instance = Cities(place=upd_city)
        city_instance.save()
    event_obj.name = upd_name
    event_obj.date = upd_date
    event_obj.info = upd_info
    event_obj.city_id = upd_city
    event_obj.save()
    message = "Event Updated!"
    return HttpResponse(message)


# @app.route('/delete', methods=["POST"])

def delete(request):
    """Gets the event object by id & deletes it."""
    eid = request.POST["id"]
    event_instance = Events.objects.get(id=eid)
    event_instance.delete()
    return HttpResponse("Event Deleted")


# @app.route("/filter_html")
def filter_html(request):
    return render(request, "filters.html", {'user_name': request.session['username']})


# @app.route("/by_date_html")
def by_date_html(request):
    return render(request, "list_by_date.html", {'user_name': request.session['username']})


def by_date(request):
    if request.method == 'POST':
        try:
            user_is = request.session['username']
            user_obj = User.objects.get(user_name=user_is)
            event_instances_list = Events.objects.filter(user_id=user_obj.user_email, date=request.POST.get('date'))
            if event_instances_list:
                return render(request, 'read.html', {'events': event_instances_list})
            else:
                return HttpResponse("No Events")
        except User.DoesNotExist:
            return HttpResponse("Please sign in to view events")


# @app.route("/by_city_html")
def by_city_html(request):
    """Through ajax:Get the cities list from Events Table."""
    cities_list = Events.objects.values("city_id").distinct()
    return render(request, "list_by_city.html", {'data': cities_list, 'user_name': request.session['username']})


def by_city(request):
    """Through ajax:Search all events with given city in Events Table."""
    if request.method == 'POST':
        try:
            user_is = request.session['username']
            user_obj = User.objects.get(user_name=user_is)
            event_instances_list = Events.objects.filter(user_id=user_obj.user_email, city_id=request.POST.get('city'))
            if event_instances_list:
                return render(request, 'read.html', {'events': event_instances_list})
            else:
                return HttpResponse("No Events")
        except User.DoesNotExist:
            return HttpResponse("Please sign in to view events")


# @app.route("/by_city_date_html")
def by_city_date_html(request):
    cities_list = Events.objects.values("city_id").distinct()
    return render(request, "list_by_city_date.html", {'data': cities_list, 'user_name': request.session['username']})


def by_date_and_city(request):
    """.ajax() call: Search all events with given date and city in Events Table."""
    if request.method == 'POST':
        try:
            user_is = request.session['username']
            user_obj = User.objects.get(user_name=user_is)
            events_list = Events.objects.filter(user_id=user_obj.user_email,
                                                date=request.POST.get('date'), city=request.POST.get('city'))
            if not events_list:
                return HttpResponse("No Events")
            else:
                return render(request, 'read.html', {'events': events_list})
        except User.DoesNotExist:
            return HttpResponse("Please sign in to view events")


def up_and_past(request):
    """Get three lists(today, upcoming, past) and renders to specific html."""
    try:
        user_is = request.session['username']
        user_obj = User.objects.get(user_name=user_is)

        today_date = str(date.today())
        today = Events.objects.filter(user_id=user_obj.user_email, date=today_date)
        upcoming = Events.objects.filter(user_id=user_obj.user_email, date__gt=today_date).order_by("date")
        past = Events.objects.filter(user_id=user_obj.user_email, date__lt=today_date).order_by('date')
        if today or upcoming or past:
            return render(request, "result.html", {'today_list': today, 'upcoming_list': upcoming, 'past_list': past})
        else:
            return HttpResponse("No Events")
    except User.DoesNotExist:
        return HttpResponse("Please sign in to view events")


def by_date_range_html(request):
    return render(request, "list_by_date_range.html", {'user_name': request.session['username']})


def by_date_range(request):
    """.ajax() call: search all events within the date range."""
    if request.method == 'POST':
        try:
            user_is = request.session['username']
            user_obj = User.objects.get(user_name=user_is)
            from_date = request.POST.get('from_date')
            to_date = request.POST.get('to_date')
            events_list = Events.objects.filter(user_id=user_obj.user_email ,date__gte=from_date, date__lte=to_date).order_by("date")
            if events_list:
                return render(request, 'read.html', {'events': events_list})
            else:
                return HttpResponse("No Events")
        except User.DoesNotExist:
            return HttpResponse("Please sign in to view events")
