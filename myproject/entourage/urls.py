from django.conf.urls.defaults import *

urlpatterns = patterns('myproject.entourage.views',
    url(r'signup', 'signup'),
    url(r'login', 'login'),
    url(r'', 'home'),
)
