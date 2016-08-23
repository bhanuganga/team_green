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
    return render(request, "add_event.html", {"data": Cities.objects.values("place")})


# @app.route('/add', methods=["POST"])

def add(request):
    data = [obj.place for obj in Cities.objects.all()]
    name = request.POST.get('name')
    date = request.POST.get('date')
    city = request.POST.get('cities')
    if city:
        city = city.capitalize()
    if city == 'Other':
        city = request.POST.get('city1').capitalize()
    info = request.POST['info']
    if city not in data:
        city_instance = Cities(place=city)
        city_instance.save()
    event_instance = Events(name=name, date=date, city=city, info=info)
    event_instance.save()
    message = "Event added!"
    return HttpResponse(message)


# @app.route("/search_event_h")          #Render search_html

def search_modify_html(request):
    return render(request, "search_modify.html", {'data': Events.objects.order_by('-date')})


# @app.route('/search', methods=['POST'])

def search(request):
    if request.method == 'POST':
        data = [obj.place for obj in Cities.objects.all()]
        eid = request.POST['event_name']
        if eid != "default":
            event_instance = Events.objects.get(id=eid)
            event_instance.date = str(event_instance.date)
            return render(request, 'search_result.html', {'instance': event_instance, 'id': eid, 'data': data})
        else:
            return HttpResponse("please select a name from list!")


# @app.route("/update", methods=["POST"])

def update(request):
    data = [obj.place for obj in Cities.objects.all()]
    upd_name = request.POST.get("upd_name")
    upd_date = request.POST.get("upd_date")
    upd_city = request.POST.get("upd_city")
    if upd_city:
        upd_city.capitalize()
    upd_info = request.POST.get("upd_info")
    eid = request.POST.get("id")

    if upd_city not in data:
        city_instance = Cities(place=upd_city)
        city_instance.save()
    event_instance = Events(id=eid, name=upd_name, date=upd_date, city=upd_city, info=upd_info)
    event_instance.save()
    message = "Event Updated!"
    return HttpResponse(message)


# @app.route('/delete', methods=["POST"])

def delete(request):
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


# @app.route("/by_city_html")
def by_city_html(request):
    cities_list = Events.objects.values("city_id").distinct()
    return render(request, "list_by_city.html", {'data': cities_list})


# @app.route("/by_city_date_html")
def by_city_date_html(request):
    cities_list = Events.objects.values("city_id").distinct()
    return render(request, "list_by_city_date.html", {'data': cities_list})


# @app.route("/by_daterange_html")
def by_daterange_html(request):
    return render(request, "list_by_daterange.html")


def by_date(request):
    if request.method == 'POST':
        event_instances_list = Events.objects.filter(date=request.POST.get('date'))
        if event_instances_list:
            return render(request, 'read.html', {'events': event_instances_list})
        else:
            return HttpResponse([])


def by_city(request):
    if request.method == 'POST':
        event_instances_list = Events.objects.filter(city=request.POST.get('city')).order_by("-date")
        if event_instances_list:
            return render(request, 'read.html', {'events': event_instances_list})
        else:
            return HttpResponse([])


def by_date_and_city(request):
    if request.method == 'POST':
        events_list = Events.objects.filter(date=request.POST.get('date'), city=request.POST.get('city'))
        if not events_list:
            return HttpResponse([])
        else:
            return render(request, 'read.html', {'events': events_list})


def by_date_range_html(request):
    return render(request, "list_by_daterange.html")


def by_date_range(request):
    if request.method == 'POST':
        date1 = request.POST.get('date1')
        date2 = request.POST.get('date2')
        events_list = Events.objects.filter(date__gt=date1).filter(date__lt=date2).order_by("date")
        if events_list:
            return render(request, 'read.html', {'events': events_list})
        else:
            return HttpResponse([])


def up_and_past(request):
    today = Events.objects.filter(date=str(date.today())).order_by("city")
    upcoming = Events.objects.filter(date__gt=str(date.today())).order_by("date")
    past = Events.objects.filter(date__lt=str(date.today())).order_by('date')
    return render(request, 'result.html', {'d1': today, 'd2': upcoming, 'd3': past})
