from myproject.socialfeed.models import Link
from django.contrib import admin

class LinkAdmin(admin.ModelAdmin):
    list_display = ['href', 'date']
    date_hierarchy = 'date' 
    ordering =('date',)

admin.site.register(Link, LinkAdmin)