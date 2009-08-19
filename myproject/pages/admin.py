from myproject.pages.models import Page
from django.contrib import admin

class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'html', 'parent']}),
        ('Advanced', {'fields': ['slug'], 'classes': ['collapse']}),
    ]
    
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Page, PageAdmin)