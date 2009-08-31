from django.conf.urls.defaults import *

# Enable the admin:
from django.contrib import admin
admin.autodiscover()

# For use with django generic views
entry_info_dict = {
        'queryset': Entry.objects.all(),
        'date_field':'pub_date',
}

# Apps
from myproject.search.views import search_site

urlpatterns = patterns('',
    (r'^$', include('myproject.pages.urls')),
    (r'^admin/filebrowser/', include('filebrowser.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^tinymce/', include('tinymce.urls')),
    (r'^search/', search_site),
    (r'^news/view/(?P<slug>[-\w]+)/$', 'django.views.generic.date_based.object_detail', entry_info_dict),
)
