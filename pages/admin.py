from django.contrib import admin
from .models import Team
from django.utils.html import format_html

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        return format_html('<img src="{}" style="width:40px; border-radius: 50px;" />', obj.photo.url)
    
    thumbnail.short_description = 'Photo'
    
    list_display = ('id', 'thumbnail', 'first_name', 'last_name', 'designation', 'created_date',)
    list_display_links = ('id', 'thumbnail', 'first_name',)
    search_fields = ('first_name', 'last_name', 'designation',)
    list_filter = ('designation',)

# Register your models here.
admin.site.register(Team, TeamAdmin)