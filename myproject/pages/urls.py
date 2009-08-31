from django.conf.urls.defaults import *

urlpatterns = patterns('myproject.pages.views',
    url(r'(?P<slug>[-\w]+)', 'serve'),
)
