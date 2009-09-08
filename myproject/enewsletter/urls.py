from django.conf.urls.defaults import *
from myproject.enewsletter.views import subscribe 

urlpatterns = patterns('myproject.enewsletter.views',
    url(r'', 'subscribe'),
    url(r'^/subscribed/', 'subscribed')
)
