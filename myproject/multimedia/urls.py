from django.conf.urls.defaults import *

urlpatterns = patterns('myproject.multimedia.views',
    # all photos or latest photos
    url(r'^$', 'photos.views.photos', name="photos"),
    # a photos details
    url(r'^details/(?P<id>\d+)/$', 'photos.views.details', name="photo_details"),
    # upload photos
    url(r'^upload/$', 'photos.views.upload', name="photo_upload"),
    #destory photo
    url(r'^destroy/(\d+)/$', 'photos.views.destroy', name='photo_destroy'),
    #edit photo
    url(r'^edit/(\d+)/$', 'photos.views.edit', name='photo_edit'),
)