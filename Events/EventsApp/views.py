# Create your views here.
from datetime import date
from django.http import HttpResponse
from django.shortcuts import render

from models import Events, Cities


# @app.route('/')
def home(request):
    return render(request, 'layout.html')


# @app.route("/add_event_h")    #Render add_event html
def add_event_html(request):
    """Add Event HTML page."""
    return render(request, "add_event.html", {"data": Cities.objects.values("place")})


# @app.route('/add', methods=["POST"])

def add(request):
    """Adding event functionality achieved through ajax call."""
    data = Cities.objects.values("place")
    name = request.POST.get('name')
    date_is = request.POST.get('date')  # variable with name "date" is shadowing inbuilt date()
    city = request.POST.get('cities')
    if city:
        city = city.capitalize()
    if city == 'Other':
        city = request.POST.get('city1').capitalize()
    info = request.POST['info']
    if city not in data:
        city_instance = Cities(place=city)
        city_instance.save()
    event_instance = Events(name=name, date=date_is, city_id=city, info=info)
    event_instance.save()
    message = "Event added!"
    return HttpResponse(message)


# @app.route("/search_event_h")          #Render search_html

def search_modify_html(request):
    """Render the list of event names in ascending order of date."""
    return render(request, "search_modify.html", {'events_list': Events.objects.order_by('date')})


# @app.route('/search', methods=['POST'])

def search(request):
    """Through ajax call: Search Event by id."""
    if request.method == 'POST':
        data = Cities.objects.values()
        event_id = request.POST["event_is"]
        if event_id != "default":
            event_instance = Events.objects.get(id=event_id)
            event_instance.date = str(event_instance.date)
            return render(request, 'search_result.html', {'instance': event_instance, 'id': event_id, 'data': data})
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

    if upd_city not in data:
        city_instance = Cities(place=upd_city)
        city_instance.save()
    event_instance = Events(id=event_id, name=upd_name, date=upd_date, city_id=upd_city, info=upd_info)
    event_instance.save()
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
    return render(request, "filters.html")


# @app.route("/by_date_html")
def by_date_html(request):
    return render(request, "list_by_date.html")


def by_date(request):
    if request.method == 'POST':
        event_instances_list = Events.objects.filter(date=request.POST.get('date'))
        if event_instances_list:
            return render(request, 'read.html', {'events': event_instances_list})
        else:
            return HttpResponse([])


# @app.route("/by_city_html")
def by_city_html(request):
    """Through ajax:Get the cities list from Events Table."""
    cities_list = Events.objects.values("city_id").distinct()
    return render(request, "list_by_city.html", {'data': cities_list})


def by_city(request):
    """Through ajax:Search all events with given city in Events Table."""
    if request.method == 'POST':
        event_instances_list = Events.objects.filter(city=request.POST.get('city')).order_by("-date")
        if event_instances_list:
            return render(request, 'read.html', {'events': event_instances_list})
        else:
            return HttpResponse([])


# @app.route("/by_city_date_html")
def by_city_date_html(request):
    cities_list = Events.objects.values("city_id").distinct()
    return render(request, "list_by_city_date.html", {'data': cities_list})


def by_date_and_city(request):
    """.ajax() call: Search all events with given date and city in Events Table."""
    if request.method == 'POST':
        events_list = Events.objects.filter(date=request.POST.get('date'), city=request.POST.get('city'))
        if not events_list:
            return HttpResponse([])
        else:
            return render(request, 'read.html', {'events': events_list})


def up_and_past(request):
    """Get three lists(today, upcoming, past) and renders to specific html."""
    today = Events.objects.filter(date=date.today()).order_by("city")
    upcoming = Events.objects.filter(date__gt=date.today()).order_by("date")
    past = Events.objects.filter(date__lt=date.today()).order_by('date')
    return render(request, "result.html", {'today_list': today, 'upcoming_list': upcoming, 'past_list': past})


def by_date_range_html(request):
    return render(request, "list_by_date_range.html")


def by_date_range(request):
    """.ajax() call: search all events within the date range."""
    if request.method == 'POST':
        date1 = request.POST.get('date1')
        date2 = request.POST.get('date2')
        events_list = Events.objects.filter(date__gte=date1, date__lte=date2).order_by("date")
        if events_list:
            return render(request, 'read.html', {'events': events_list})
        else:
            return HttpResponse([])
