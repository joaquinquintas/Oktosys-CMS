from django.conf.urls.defaults import *
from myproject.pages.views import serve 

urlpatterns = patterns('myproject.pages.views',
    url(r'(?P<slug>[-\w]+)', 'serve', name="pages-root"),
)
