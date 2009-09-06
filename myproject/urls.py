from django.conf.urls.defaults import *
from django.conf import settings
from haystack.views import SearchView
# Enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    (r'^$', 'myproject.pages.views.home'),
    (r'^pages/', include('myproject.pages.urls')),
    (r'^admin/filebrowser/', include('filebrowser.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^tinymce/', include('tinymce.urls')),
    (r'^news/', include('myproject.news.urls')),
    (r'^entourage/', include('myproject.entourage.urls')),
    (r'^multimedia/', include('myproject.multimedia.urls')),
    url(r'^search/', SearchView(), name="haystack_search"),
    (r'^xml/homeflash.xml', 'django.views.generic.simple.direct_to_template', {'template': 'pages/homeflash.xml'}),

)
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
