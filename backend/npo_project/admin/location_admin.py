from django.contrib import admin

from ..models import Location


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('address',)
    search_fields = ('address',)
