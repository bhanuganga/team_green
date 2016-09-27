# Create your views here.
import datetime
from django.http import HttpResponse
from django.shortcuts import render
from models import *

def index(request):
    list_hotels = Hotel.objects.all()
    return render(request,'index.html',{'list_hotels':list_hotels})

def hotels_list(request):
    list_of_hotels=Hotel.objects.all()
    return render(request,'hotel_list.html',{'list_of_hotels':list_of_hotels})

def hotels_result(request):
    if request.method == 'POST':
        eid = request.POST.get('hotel_name')
        if eid != "default":
            details=Hotel.objects.get(Name=request.POST.get('hotel_name'))
            return render(request,'hotels_result.html',{'details':details})
        else:
            return HttpResponse("please select a hotel from list!")
def add_hotel(request):
    if request.method=='POST':
        newhotel=request.POST.get('newhotel')
        newrent=request.POST.get('newrent')
        list_of_hotels=[obj.Name for obj in Hotel.objects.all()]
        if newhotel not in list_of_hotels:
            Hotel(Name=newhotel,Rent=newrent).save()
            return HttpResponse('HOTEL ADDED')

def booking(request):
    if request.method=='POST':
        name=request.POST.get('name')
        rent=request.POST.get('rent')
        persons=request.POST.get('persons')
        fromdate= datetime.datetime.strptime(request.POST.get('fromdate'), "%Y-%m-%d")
        todate=datetime.datetime.strptime(request.POST.get('todate'), "%Y-%m-%d")
        days=(todate-fromdate).days
        total=int(rent)*int(days)*int(persons)
        instance=Booking(Hotel_name_id=name,Days=days,from_date=fromdate,to_date=todate,Persons=persons,Total=str(total))
        instance.save()
        message='Yours total amount Rs.{}'.format(total)
        return HttpResponse(message)

def cart(request):
    total_amount=0
    total_list=Booking.objects.all()
    list_of_prices=list(Booking.objects.values('Total'))
    for i in range(0,len(list_of_prices)):
        total_amount+=list_of_prices[i]['Total']
    return render(request,'cart.html',{'total_list':total_list,'total_amount':total_amount})

def clear(request):
    list=Booking.objects.all()
    list.delete()
    return HttpResponse('data deleted')