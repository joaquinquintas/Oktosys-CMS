from django.conf.urls.defaults import *

urlpatterns = patterns('myproject.entourage.views',
    url(r'signup', 'riders_new'),
    url(r'login', 'login'),
)