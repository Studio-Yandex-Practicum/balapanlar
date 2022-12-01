from django import forms
from django.contrib import admin

from balapanlar.settings import EMPTY_VALUE_ADMIN_PANEL
from ..models import Location


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        exclude = ('id', 'latitude', 'longitude', 'full_address')


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    form = LocationForm
    list_display = (
        'full_address', 'center_name', 'address', 'additional_info'
    )
    list_editable = ('center_name', 'address', 'additional_info')
    search_fields = ('full_address',)
    empty_value_display = EMPTY_VALUE_ADMIN_PANEL
