from myproject.multimedia.models import Tag
from django.contrib import admin

class TagAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tag, TagAdmin)