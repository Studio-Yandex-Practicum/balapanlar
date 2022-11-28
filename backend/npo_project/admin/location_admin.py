from django import forms
from django.contrib import admin

from ..models import Location


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        exclude = ('id', 'latitude', 'longitude')


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    form = LocationForm
    list_display = ('adress', 'image', 'latitude', 'longitude')
    search_fields = ('adress',)
