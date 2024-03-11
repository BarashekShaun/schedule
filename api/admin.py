from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import AdvUser, Organization, Event


admin.site.register(AdvUser)
admin.site.register(Organization)


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date',)
    list_display_links = ('title',)
    ordering = ['-date', 'title']
    search_fields = ['title']
    readonly_fields = ['preview']

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')


admin.site.register(Event, EventAdmin)
