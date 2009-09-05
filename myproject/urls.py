from django.conf.urls.defaults import *
from django.conf import settings

# Enable the admin:
from django.contrib import admin
admin.autodiscover()

# Apps
from myproject.search.views import search_site

urlpatterns = patterns('',
    (r'^$', 'myproject.pages.views.home'),
    (r'^pages/', include('myproject.pages.urls')),
    (r'^admin/filebrowser/', include('filebrowser.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^tinymce/', include('tinymce.urls')),
    (r'^search/', search_site),
    (r'^news/', include('myproject.news.urls')),
    (r'^entourage/', include('myproject.entourage.urls')),
    (r'^multimedia/', include('myproject.multimedia.urls')),

)
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
