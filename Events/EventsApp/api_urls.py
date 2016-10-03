from django.conf.urls import url, patterns


urlpatterns = patterns('EventsApp.views',
                       url(r'^add$', 'add', name="add_api"),
                       url(r'^search$', 'search', name="search_api"),
                       url(r'^delete$', 'delete', name="delete_api"),
                       url(r'^update$', 'update', name="update_api"),
                       url(r'^by_date$', 'by_date', name='by_date_api'),
                       url(r'^by_city$', 'by_city', name="by_city_api"),
                       url(r'^by_date_and_city$', 'by_date_and_city', name="by_date_and_city_api"),
                       url(r'^by_date_range$', 'by_date_range', name="by_date_range_api"),
                       )
