from django.conf.urls.defaults import *

urlpatterns = patterns('pages.views',
    url(r'^$', 'home'),
)
