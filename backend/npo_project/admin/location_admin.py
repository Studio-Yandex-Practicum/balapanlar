from django import forms
from django.contrib import admin
from django.utils.html import format_html
from sorl.thumbnail import get_thumbnail

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
        'full_address',
        'center_name',
        'address',
        'additional_info',
        'image',
        'preview',
        'schema_description'
    )
    list_editable = (
        'center_name',
        'address',
        'additional_info',
        'image',
        'schema_description'
    )
    search_fields = ('full_address',)
    empty_value_display = EMPTY_VALUE_ADMIN_PANEL

    def preview(self, obj):
        if obj.image:
            image = get_thumbnail(
                obj.image, '200x200', upscale=False, crop=False, quality=100
            )
            return format_html(
                f'<img src="{image.url}" '
                f'width="{image.width}" height="{image.height}">'
            )
        return 'Схема не сохранена'
    preview.allow_tags = True
    preview.short_description = 'Предпросмотр схемы проезда'
