from django.conf.urls.defaults import *

# Enable the admin:
from django.contrib import admin
admin.autodiscover()

# Apps
from myproject.search.views import search_site

urlpatterns = patterns('',
    (r'^$', 'myproject.pages.views.home'),
    (r'^fbconnect/', include('myproject.pyfacebook.urls')),
    (r'^pages/', include('myproject.pages.urls')),
    (r'^admin/filebrowser/', include('filebrowser.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^tinymce/', include('tinymce.urls')),
    (r'^search/', search_site),
    (r'^news/', include('myproject.news.urls')),
    (r'^entourage/', include('myproject.entourage.urls')),
    (r'^multimedia/', include('myproject.multimedia.urls')),
)
