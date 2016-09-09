from django.http import HttpResponse
from django.http.response import Http404
from django.shortcuts import render
from .models import AddEvent, Cities, User
import datetime


def signed(request):
    username = request.POST.get('username')
    email_id = request.POST.get('email_id')
    ph_no = request.POST.get('ph_no')
    password = request.POST.get('password')
    User.objects.create(username=username, email_id=email_id, ph_no=ph_no, password=password)
    return HttpResponse("Signed in")


def logged_in(request):
    if request.method != "POST":
        raise Http404("Only POSTs are allowed")
    try:
        email_id = request.POST.get('email_id')
        password = request.POST.get('password')
        user_instance = User.objects.get(email_id=email_id, password=password)
        if user_instance.password == password:
            request.session['username'] = user_instance.username
            name = request.session.get('username')
            return HttpResponse(name)
        else:
            return HttpResponse("Your username and password doesn't match")
    except User.DoesNotExist:
        return HttpResponse("Register to login")


def logout(request):
    if 'username' in request.session.keys():
        name = request.session.get('username')
        del request.session['username']
        data = "{} Logged out".format(name)
        return render(request, 'logout.html',{'data': data})


def index(request):
    if request.session.get('username'):
        return render(request, 'layout.html', {'name': request.session.get('username')})
    else:
        return render(request, 'layout.html', {'name': ''})


def add_event_html(request):
    if request.session.get('username'):
        return render(request, "add_event.html", {'data': Cities.objects.all(), 'name': request.session.get('username')})
    else:
        return render(request, 'add_event.html',{'data': Cities.objects.all(), 'name': ''})


def add(request):
    if request.session.get('username'):
        username = request.session.get('username')
        user_instance = User.objects.get(username=username)
        user_info_id = user_instance.email_id
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

        AddEvent.objects.create(name=name, city=city, date=date, info=info, user_info_id=user_info_id)

        return HttpResponse("Event added!")
    else:
        return HttpResponse('Login to add event.')

########################


def search_html(request):
    if request.session.get('username'):
        username = request.session.get('username')
        user_instance = User.objects.get(username=username)
        return render(request, "search_modify.html", {'data': AddEvent.objects.filter(user_info_id=user_instance.email_id), 'name': username})
    else:
        return render(request, 'search_modify.html', {'data': AddEvent.objects.all(), 'name': ''})


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
    if request.session.get('username'):
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
    else:
        return HttpResponse('Login to update event.')


def delete(request):
    if request.session.get('username'):
        id = request.POST.get("id")

        AddEvent.objects.filter(id=id).delete()

        return HttpResponse("Deleted")
    else:
        return HttpResponse('Login to delete event.')


###########################


def filter_html(request):
    if request.session.get('username'):
        username = request.session.get('username')
        return render(request, "filters.html", {'data': AddEvent.objects.all(), 'name': username})
    else:
        return render(request, 'filters.html', {'data': AddEvent.objects.all(), 'name': ''})


def by_date_html(request):
    if request.session.get('username'):
        username = request.session.get('username')
        return render(request, "list_by_date.html", {'data': AddEvent.objects.all(), 'name': username})
    else:
        return render(request, 'list_by_date.html', {'data': AddEvent.objects.all(), 'name': ''})


def by_date(request):
    if request.method == 'POST':
        date1 = request.POST.get('date')
        if request.session.get('username'):
            username = request.session.get('username')
            user_instance = User.objects.get(username=username)
            user_info = user_instance.email_id
            filter_data = AddEvent.objects.filter(date=date1, user_info=user_info)
        else:
            filter_data = AddEvent.objects.filter(date=date1)

        if not filter_data:
            return HttpResponse('no event found')
        else:
            return render(request, 'read.html', {'data': filter_data})


#####################


def by_city_html(request):
    if request.session.get('username'):
        username = request.session.get('username')
        return render(request, "list_by_city.html", {'data': Cities.objects.all(), 'name': username})
    else:
        return render(request, 'list_by_city.html', {'data': Cities.objects.all(), 'name': ''})


def by_city(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        if request.session.get('username'):
            username = request.session.get('username')
            user_instance = User.objects.get(username=username)
            user_info = user_instance.email_id
            filter_data = AddEvent.objects.filter(city=city, user_info=user_info)
        else:
            filter_data = AddEvent.objects.filter(city=city)
        if not filter_data:
            return HttpResponse('no event found')
        else:
            return render(request, 'read.html', {'data': filter_data})


#####################


def by_city_date_html(request):
    if request.session.get('username'):
        username = request.session.get('username')
        return render(request, "list_by_city_date.html", {'data': Cities.objects.all(), 'name': username})
    else:
        return render(request, 'list_by_city_date.html', {'data': Cities.objects.all(), 'name': ''})


def by_date_and_city(request):
    if request.method == 'POST':
        date1 = request.POST.get('date')
        city = request.POST.get('city')
        if request.session.get('username'):
            username = request.session.get('username')
            user_instance = User.objects.get(username=username)
            user_info = user_instance.email_id
            filter_data = AddEvent.objects.filter(date=date1, city=city, user_info=user_info)
        else:
            filter_data = AddEvent.objects.filter(date=date1, city=city)

        if not filter_data:
            return HttpResponse('no event found')
        else:
            return render(request, 'read.html', {'data': filter_data})


#########################


def by_date_range_html(request):
    if request.session.get('username'):
        username = request.session.get('username')
        return render(request, "list_by_daterange.html", {'name': username})
    else:
        return render(request, 'list_by_daterange.html', {'name': ''})


def by_date_range(request):
    if request.method == 'POST':
        date1 = request.POST.get('fromdate')
        date2 = request.POST.get('todate')
        if date1 > date2:
            date1,date2 = date2,date1
        if request.session.get('username'):
            username = request.session.get('username')
            user_instance = User.objects.get(username=username)
            user_info = user_instance.email_id
            filter_data = AddEvent.objects.filter(date__gte=date1, date__lte=date2, user_info=user_info).order_by('-date')
        else:
            filter_data = AddEvent.objects.filter(date__gte=date1, date__lte=date2).order_by('-date')

        if not filter_data:
            return HttpResponse('no event found')
        else:
            return render(request, 'read.html', {'data': filter_data})


#######################


def up_and_past(request):
    date1 = datetime.date.today()
    if request.session.get('username'):
        username = request.session.get('username')
        user_instance = User.objects.get(username=username)
        user_info = user_instance.email_id
        filter_data_today = AddEvent.objects.filter(date=date1, user_info=user_info).order_by('-date')
        filter_data_upcome = AddEvent.objects.filter(date__gt=date1, user_info=user_info).order_by('-date')
        filter_data_past = AddEvent.objects.filter(date__lt=date1, user_info=user_info).order_by('-date')
        return render(request, 'read_all.html', {'data1': filter_data_today, 'data2': filter_data_upcome, 'data3': filter_data_past, 'name': username})

    else:
        filter_data_today = AddEvent.objects.filter(date=date1).order_by('-date')
        filter_data_upcome = AddEvent.objects.filter(date__gt=date1).order_by('-date')
        filter_data_past = AddEvent.objects.filter(date__lt=date1).order_by('-date')
        return render(request, 'read_all.html', {'data1': filter_data_today, 'data2': filter_data_upcome, 'data3': filter_data_past,'name': ''})

##############################
