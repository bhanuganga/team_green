from django.http import HttpResponse
from django.shortcuts import render
from .models import AddEvent, Cities
import datetime


def index(request):
    return render(request, 'layout.html', {})


def add_event_html(request):
    return render(request, "add_event.html", {'data': Cities.objects.all()})


def add(request):
    name = request.POST.get('name')
    date = request.POST.get('date')
    info = request.POST.get('info')
    city = request.POST.get('cities')

    if city:
        city = city.capitalize()
    if city == 'Other':
        city = request.POST.get('city1').capitalize()

    if city not in [obj.city for obj in Cities.objects.all()]:
        Cities.objects.create(city=city)

    AddEvent.objects.create(name=name, city=city, date=date, info=info)

    message = "Event added!"
    return HttpResponse(message)


########################


def search_html(request):
    return render(request, "search_modify.html", {'data': AddEvent.objects.all()})


def search(request):
    if request.method == 'POST':
        eid = request.POST.get('event_name')
        if eid != "default":
            event_instance = AddEvent.objects.get(id=eid)
            event_instance.date = str(event_instance.date)
            return render(request, 'search_result.html', {'instance': event_instance, 'id': eid, 'data': Cities.objects.all()})
        else:
            return HttpResponse("please select a name from list!")


def update(request):
    upd_name = request.POST.get("upd_name")
    upd_date = request.POST.get("upd_date")
    upd_city = request.POST.get("upd_city")
    if upd_city:
        upd_city = upd_city.capitalize()
    upd_info = request.POST.get("upd_info")
    eid = request.POST.get("id")
    if upd_city not in [obj.city for obj in Cities.objects.all()]:
        Cities.objects.create(city=upd_city)

    AddEvent.objects.filter(id=eid).update(name=upd_name, date=upd_date, city=upd_city, info=upd_info)

    return HttpResponse("Updated")


def delete(request):
    eid = request.POST.get("id")

    AddEvent.objects.filter(id=eid).delete()

    return HttpResponse("Deleted")


###########################


def filter_html(request):
    return render(request, "filters.html", {'data': AddEvent.objects.all()})


def by_date_html(request):
    return render(request, "list_by_date.html", {'data': AddEvent.objects.all()})


def by_date(request):
    if request.method == 'POST':
        a = AddEvent.objects.filter(date=request.POST.get('date'))
        if not a:
            return HttpResponse('no event found')
        else:
            return render(request, 'read.html', {'d': a})


#####################


def by_city_html(request):
    return render(request, "list_by_city.html", {'data': Cities.objects.all()})


def by_city(request):
    if request.method == 'POST':
        a = AddEvent.objects.filter(city=request.POST.get('city'))
        if not a:
            return HttpResponse('no event found')
        else:
            return render(request, 'read.html', {'d': a})


#####################


def by_city_date_html(request):
    return render(request, "list_by_city_date.html", {'data': Cities.objects.all()})


def by_date_and_city(request):
    if request.method == 'POST':
        a = AddEvent.objects.filter(date=request.POST.get('date'), city=request.POST.get('city'))
        if not a:
            return HttpResponse('no event found')
        else:
            return render(request, 'read.html', {'d': a})


#########################


def by_date_range_html(request):
    return render(request, "list_by_daterange.html")


def by_date_range(request):
    if request.method == 'POST':
        date1 = request.POST.get('fromdate')
        date2 = request.POST.get('todate')
        if date1 > date2:
            date1,date2 = date2,date1

        a = AddEvent.objects.filter(date__gte=date1, date__lte=date2).order_by('-date')
        if not a:
            return HttpResponse('no event found')
        else:
            return render(request, 'read.html', {'d': a})


#######################


def up_and_past(request):
    date1 = datetime.datetime.today()
    a1 = AddEvent.objects.filter(date=date1).order_by('-date')
    a2 = AddEvent.objects.filter(date__gt=date1).order_by('-date')
    a3 = AddEvent.objects.filter(date__lt=date1).order_by('-date')

    return render(request, 'result.html', {'d1': a1, 'd2': a2, 'd3': a3})


##############################
