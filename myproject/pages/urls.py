from django.conf.urls.defaults import *
from myproject.pages.views import serve 

urlpatterns = patterns('myproject.pages.views',
    url(r'$', 'serve', name="pages-root"),
    url(r'^(?P<path>.*)$', 'serve',
        name='pages-details-by-path'),
)
