from myproject.news.models import Entry
from django.contrib import admin

class EntryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['headline', 'excerpt', 'article', 'is_published']}),
        ('Advanced', {'fields': ['slug'], 'classes': ['collapse']}),
    ]

    prepopulated_fields = {'slug': ('headline',)}

admin.site.register(Entry, EntryAdmin)