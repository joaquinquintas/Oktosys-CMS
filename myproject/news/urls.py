from django.conf.urls.defaults import *

urlpatterns = patterns('myproject.news.views',
    url(r'(?P<slug>[-\w]+)', 'view'),
)
