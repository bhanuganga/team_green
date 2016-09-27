from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from hotel_app.views import *

admin.autodiscover()

urlpatterns = [
    url(r'^$',index,name='index'),
    url(r'^hotels_list$',hotels_list,name='hotels_list'),
    url(r'^hotels_result$',hotels_result,name='hotels_result'),
    url(r'^cart$',cart,name='cart'),
    url(r'^booking$',booking,name='booking'),
    url(r'^clear$',clear,name='clear'),
    url(r'^add_hotel$',add_hotel,name='add_hotel')
]