from models import Photo, Video
from django.contrib import admin

class PhotoAdmin(admin.ModelAdmin):
    pass

class VideoAdmin(admin.ModelAdmin):
    fields = ('url',)

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Video, VideoAdmin)
