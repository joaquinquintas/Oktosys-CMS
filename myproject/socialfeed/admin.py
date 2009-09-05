from myproject.socialfeed.models import Link
from django.contrib import admin

class LinkAdmin(admin.ModelAdmin):
    list_display = ['href', 'provider_rule', 'published', 'author']
    list_filter = ['published', 'provider_rule']
    date_hierarchy = 'published' 
    ordering = ('provider_rule', 'published',)

admin.site.register(Link, LinkAdmin)