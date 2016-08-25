from django.conf.urls import url, patterns, include

urlpatterns = patterns('EventsApp.views',
                       url(r'^$', 'home'),
                       url(r'^add_event_html$', 'add_event_html', name="eventsapp_add_event_html"),
                       url(r'^search_modify_html$', 'search_modify_html', name="eventsapp_search_modify_html"),
                       url(r'^by_date_html$', 'by_date_html', name="eventsapp_by_date_html"),
                       url(r'^by_city_html$', 'by_city_html', name="eventsapp_by_city_html"),
                       url(r'^by_city_date_html', 'by_city_date_html', name="eventsapp_by_city_date_html"),
                       url(r'^up_and_past$', 'up_and_past', name="eventsapp_up_and_past"),
                       url(r'^by_date_range_html$', 'by_date_range_html', name="eventsapp_by_date_range_html"),
                       url(r'^api/', include('EventsApp.api_urls'))
                       )
