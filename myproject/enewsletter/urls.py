from django.conf.urls.defaults import *
from myproject.enewsletter.views import subscribe, subscribed

urlpatterns = patterns('myproject.enewsletter.views',
    url(r'subscribed', 'subscribed'),
    url(r'', 'subscribe'),
)
