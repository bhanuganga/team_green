from datetime import date
from django.core.urlresolvers import reverse
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from models import *


def index(request):
    if request.session.get('member_id'):

        return render(request, 'mainpage.html', {'user': request.session.get('member_id')})
    else:
        return render(request, 'mainpage.html',{'user':''})


def createaccount(request):
    username=request.POST.get('username')
    email=request.POST.get('email')
    mobile=request.POST.get('mobile')
    password=request.POST.get('password')
    list_of_mails=[emailid for emailid in Member.objects.values('e_mail')]
    if email not in list_of_mails:
        instance=Member(user_name=username,mobile=mobile,e_mail=email,password=password)
        instance.save()
        return HttpResponse('Sucessfully Created')
    else:
        return HttpResponse('Already Registered')

def login(request):
    if request.method!="POST":
        raise Http404("Only POSTs are allowed")
    try:
        m = Member.objects.get(e_mail=request.POST.get('email'))
        if m.password == request.POST.get('password'):
            request.session['member_id'] = m.user_name
            return HttpResponse("logged in")
        else:
            return  HttpResponse("Your username and password doesn't match")
    except Member.DoesNotExist:
        return HttpResponse("Please Register")

def logout(request):
    try:
        if 'member_id' in request.session.keys():
            del request.session['member_id']
    except KeyError:
        pass
    return HttpResponseRedirect(reverse('index'))


def add_event_html(request):
    if request.session.get('member_id'):
        return render(request, "add_event.html", {'data': Cities.objects.all(), 'user': request.session.get('member_id')})
    else:
        return render(request, "add_event.html", {'data': Cities.objects.all(), 'user': ''})


def add(request):
    data = [obj.city for obj in Cities.objects.all()]
    m=request.session.get('member_id')
    if m:
        user_id=Member.objects.get(user_name=m).e_mail
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
        event_instance = Event(event_name=name, event_date=date, event_city=city, event_info=info,user_id=user_id)
        event_instance.save()
        message = "Event added!"
        return HttpResponse(message)
    else:
        return HttpResponse('Please login to add')


def search_html(request):

    if request.session.get('member_id'):
        user_id = Member.objects.get(user_name=request.session.get('member_id')).e_mail
        return render(request, "search_modify.html", {'data': Event.objects.filter(user_id=user_id), 'user': request.session.get('member_id')})
    else:
        return render(request, "search_modify.html", {'data': Event.objects.all(), 'user': ''})


def search(request):
    if request.method == 'POST':
        eid = request.POST.get('event_name')
        if eid != "default":
            event_instance = Event.objects.get(id=eid)
            event_instance.event_date = str(event_instance.event_date)
            return render(request, 'search_result.html', {'instance': event_instance, 'id': eid, 'data': Cities.objects.all()})
        else:
            return HttpResponse("please select a name from list!")


def update(request):
    data = [obj.city for obj in Cities.objects.all()]
    m = request.session.get('member_id')
    if m:
        upd_name = request.POST.get("upd_name")
        upd_date = request.POST.get("upd_date")
        upd_city = request.POST.get("upd_city")
        if upd_city:
            upd_city=upd_city.capitalize()
        upd_info = request.POST.get("upd_info")
        eid = request.POST.get("id")
        email=request.POST.get('email')

        if upd_city not in data:
            data = Cities(city=upd_city)
            data.save()
        temp_dict = Event(id=eid,user_id=email,event_name=upd_name, event_date=upd_date, event_city=upd_city, event_info=upd_info)
        temp_dict.save()
        message = 'EVENT UPDATED'
        return HttpResponse(message)
    else:
        return HttpResponse('Please login')


def delete(request):
    m = request.session.get('member_id')
    if m:
        eid = request.POST["id"]
        Event.objects.get(id=eid).delete()
        message = 'EVENT DELETED'
        return HttpResponse(message)
    else:
        return HttpResponse('Please login')


def filter_html(request):
    if request.session.get('member_id'):
        return render(request, "filters.html", {'user': request.session.get('member_id')})
    else:
        return render(request, "filters.html",{'user':''})


def by_date_html(request):
    if request.session.get('member_id'):
        return render(request, "list_by_date.html", {'user': request.session.get('member_id')})
    else:
        return render(request, "list_by_date.html", {'user': ''})


def by_date(request):
    if request.method == 'POST':
        list = Event.objects.filter(event_date=request.POST.get('date'))
        if not list:
            return HttpResponse('no event found')
        else:
            return render(request, 'read.html', {'list': list})


def by_city_html(request):
    if request.session.get('member_id'):
        return render(request, "list_by_city.html", {'data': Cities.objects.all(), 'user': request.session.get('member_id')})
    else:
        return render(request, "list_by_city.html", {'data': Cities.objects.all(),'user':''})


def by_city(request):
    if request.method == 'POST':
        list = Event.objects.filter(event_city=request.POST.get('city')).order_by('event_date')
        if not list:
            return HttpResponse('no event found')
        else:

            return render(request, 'read.html', {'list': list})


def by_city_date_html(request):
    if request.session.get('member_id'):
        return render(request, "list_by_city_date.html", {'data': Cities.objects.all(), 'user': request.session.get('member_id')})
    else:
        return render(request, "list_by_city_date.html", {'data': Cities.objects.all(),'user':''})


def by_date_and_city(request):
    if request.method == 'POST':
        list = Event.objects.filter(event_date=request.POST.get('date'), event_city=request.POST.get('city'))
        if not list:
            return HttpResponse('no event found')
        else:

            return render(request, 'read.html', {'list': list})


def by_date_range_html(request):
    if request.session.get('member_id'):
        return render(request, "list_by_daterange.html", {'data': Event.objects.all(), 'user': request.session.get('member_id')})
    else:
        return render(request, "list_by_daterange.html", {'data': Event.objects.all(),'user':''})


def by_date_range(request):
    if request.method == 'POST':
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        if fromdate>todate:
            fromdate,todate=todate,fromdate
        list = Event.objects.filter(event_date__gte=fromdate).filter(event_date__lte=todate).order_by('event_date')
        if not list:
            return HttpResponse('no event found')
        else:
            return render(request, 'read.html', {'list': list})


def up_and_past(request):

    today = Event.objects.filter(event_date=date.today()).order_by('event_date')
    upcoming = Event.objects.filter(event_date__gt=date.today()).order_by('event_date')
    past = Event.objects.filter(event_date__lt=date.today()).order_by('event_date')
    if request.session.get('member_id'):
        return render(request, 'up_and_past.html', {'today': today, 'upcoming': upcoming, 'past': past, 'user': request.session.get('member_id')})
    else:
        return render(request, 'up_and_past.html', {'today': today, 'upcoming': upcoming, 'past': past, 'user': ''})

