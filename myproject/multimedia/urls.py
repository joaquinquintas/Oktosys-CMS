from django.conf.urls.defaults import *

urlpatterns = patterns('myproject.multimedia.views',
    url(r'photos/(\d+)/(\d+)', 'photo_view'),
    url(r'', 'index'),
)