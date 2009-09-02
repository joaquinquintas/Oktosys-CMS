from models import Photo
from django.contrib import admin

class PhotoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Photo, PhotoAdmin)
