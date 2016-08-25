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
        id = request.POST.get('event_name')
        if id != "default":
            event_instance = AddEvent.objects.get(id=id)
            event_instance.date = str(event_instance.date)
            return render(request, 'search_result.html', {'instance': event_instance, 'id': id, 'data': Cities.objects.all()})
        else:
            return HttpResponse("please select a name from list!")


def update(request):
    upd_name = request.POST.get("upd_name")
    upd_date = request.POST.get("upd_date")
    upd_city = request.POST.get("upd_city")
    if upd_city:
        upd_city = upd_city.capitalize()
    upd_info = request.POST.get("upd_info")
    id = request.POST.get("id")
    if upd_city not in [obj.city for obj in Cities.objects.all()]:
        Cities.objects.create(city=upd_city)

    AddEvent.objects.filter(id=id).update(name=upd_name, date=upd_date, city=upd_city, info=upd_info)

    return HttpResponse("Updated")


def delete(request):
    id = request.POST.get("id")

    AddEvent.objects.filter(id=id).delete()

    return HttpResponse("Deleted")


###########################


def filter_html(request):
    return render(request, "filters.html", {'data': AddEvent.objects.all()})


def by_date_html(request):
    return render(request, "list_by_date.html", {'data': AddEvent.objects.all()})


def by_date(request):
    if request.method == 'POST':
        date1 = request.POST.get('date')
        filter_data = AddEvent.objects.filter(date=date1)
        if not filter_data:
            return HttpResponse('no event found')
        else:
            return render(request, 'read.html', {'data': filter_data})


#####################


def by_city_html(request):
    return render(request, "list_by_city.html", {'data': Cities.objects.all()})


def by_city(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        filter_data = AddEvent.objects.filter(city=city)
        if not filter_data:
            return HttpResponse('no event found')
        else:
            return render(request, 'read.html', {'data': filter_data})


#####################


def by_city_date_html(request):
    return render(request, "list_by_city_date.html", {'data': Cities.objects.all()})


def by_date_and_city(request):
    if request.method == 'POST':
        date1 = request.POST.get('date')
        city = request.POST.get('city')
        filter_data = AddEvent.objects.filter(date=date1, city=city)
        if not filter_data:
            return HttpResponse('no event found')
        else:
            return render(request, 'read.html', {'data': filter_data})


#########################


def by_date_range_html(request):
    return render(request, "list_by_daterange.html")


def by_date_range(request):
    if request.method == 'POST':
        date1 = request.POST.get('fromdate')
        date2 = request.POST.get('todate')
        if date1 > date2:
            date1,date2 = date2,date1

        filter_data = AddEvent.objects.filter(date__gte=date1, date__lte=date2).order_by('-date')
        if not filter_data:
            return HttpResponse('no event found')
        else:
            return render(request, 'read.html', {'data': filter_data})


#######################


def up_and_past(request):
    date1 = datetime.datetime.today()
    filter_data_today = AddEvent.objects.filter(date=date1).order_by('-date')
    filter_data_upcome = AddEvent.objects.filter(date__gt=date1).order_by('-date')
    filter_data_past = AddEvent.objects.filter(date__lt=date1).order_by('-date')

    return render(request, 'read_all.html', {'data1': filter_data_today, 'data2': filter_data_upcome, 'data3': filter_data_past})


##############################
