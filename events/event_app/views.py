from datetime import date

from django.http import HttpResponse
from django.shortcuts import render
from models import *


def index(request):
    return render(request, 'layout.html', {})


def add_event_html(request):
    return render(request, "add_event.html", {'data': Cities.objects.all()})


def add(request):
    data = [city.city for city in Cities.objects.all()]
    name = request.POST.get('name')
    date = request.POST.get('date')
    city = request.POST.get('cities')
    if city:
        city = city.capitalize()
    if city == 'Other':
        city = request.POST.get('city1').capitalize()
    info = request.POST.get('info')
    if city not in data:
        data = Cities(city=city)
        data.save()
    event_instance = Event(event_name=name, event_date=date, event_city=city, event_info=info)
    event_instance.save()
    message = "Event added!"
    return HttpResponse(message)


def search_html(request):
    return render(request, "search_modify.html", {'data': Event.objects.all()})


def search(request):
    if request.method == 'POST':

        eid = request.POST['event_name']
        if eid != "default":
            event_instance = Event.objects.get(id=eid)
            event_instance.event_date = str(event_instance.event_date)
            return render(request, 'search_result.html', {'instance': event_instance, 'id': eid, 'data': Cities.objects.all()})
        else:
            return HttpResponse("please select a name from list!")


def update(request):
    data = [city.city for city in Cities.objects.all()]
    upd_name = request.POST.get("upd_name")
    upd_date = request.POST.get("upd_date")
    upd_city = request.POST.get("upd_city")
    if upd_city:
        upd_city=upd_city.capitalize()
    upd_info = request.POST.get("upd_info")
    eid = request.POST.get("id")

    if upd_city not in data:
        data = Cities(city=upd_city)
        data.save()
    temp_dict = Event(id=eid,event_name=upd_name, event_date=upd_date, event_city=upd_city, event_info=upd_info)
    temp_dict.save()
    message = 'EVENT UPDATED'
    return HttpResponse(message)


def delete(request):
    eid = request.POST["id"]
    Event.objects.get(id=eid).delete()
    message = 'EVENT DELETED'
    return HttpResponse(message)


def filter_html(request):
    return render(request, "filters.html")


def by_date_html(request):
    return render(request, "list_by_date.html")


def by_date(request):
    if request.method == 'POST':
        list = Event.objects.filter(event_date=request.POST.get('date'))
        if not list:
            return HttpResponse('no event found')
        else:
            return render(request, 'read.html', {'d': list})


def by_city_html(request):
    return render(request, "list_by_city.html", {'data': Cities.objects.all()})


def by_city(request):
    if request.method == 'POST':
        list = Event.objects.filter(event_city=request.POST.get('city')).order_by('event_date')
        if not list:
            return HttpResponse('no event found')
        else:

            return render(request, 'read.html', {'d': list})


def by_city_date_html(request):
    return render(request, "list_by_city_date.html", {'data': Cities.objects.all()})


def by_date_and_city(request):
    if request.method == 'POST':
        list = Event.objects.filter(event_date=request.POST.get('date'), event_city=request.POST.get('city'))
        if not list:
            return HttpResponse('no event found')
        else:

            return render(request, 'read.html', {'d': list})


def by_date_range_html(request):
    return render(request, "list_by_daterange.html", {'data': Event.objects.all()})


def by_date_range(request):
    if request.method == 'POST':
        date1 = request.POST.get('date1')
        date2 = request.POST.get('date2')
        if date1>date2:
            date1,date2=date2,date1
        list = Event.objects.filter(event_date__gte=date1).filter(event_date__lte=date2).order_by('event_date')
        if list == []:
            return HttpResponse('no event found')
        else:
            return render(request, 'read.html', {'d': list})


def up_and_past(request):
    d = Event.objects.filter(event_date=date.today()).order_by('event_date')
    d1 = Event.objects.filter(event_date__gt=date.today()).order_by('event_date')
    d2 = Event.objects.filter(event_date__lt=date.today()).order_by('event_date')

    return render(request, 'result.html', {'d1': d, 'd2': d1, 'd3': d2})
