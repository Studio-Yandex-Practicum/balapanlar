from django.contrib import admin

from balapanlar.settings import EMPTY_VALUE_ADMIN_PANEL
from ..models import Location


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'full_address', 'address_for_center', 'address', 'additional_info'
    )
    list_editable = ('address_for_center', 'address', 'additional_info')
    search_fields = ('full_address',)
    empty_value_display = EMPTY_VALUE_ADMIN_PANEL
