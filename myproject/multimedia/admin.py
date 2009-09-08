from myproject.multimedia.models import Photo, Video
from django.contrib import admin

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_slug', 'caption','date_added','member','tags',)    

class VideoAdmin(admin.ModelAdmin):
    fields = ('url',)

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Video, VideoAdmin)
