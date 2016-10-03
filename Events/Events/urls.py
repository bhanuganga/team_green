from django.conf.urls import include, url, patterns

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^', include("EventsApp.urls")),
                       )
