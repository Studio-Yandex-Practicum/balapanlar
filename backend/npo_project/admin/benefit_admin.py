from sorl.thumbnail import get_thumbnail

from django.contrib import admin
from django.utils.html import format_html

from balapanlar.settings import EMPTY_VALUE_ADMIN_PANEL
from ..models import Benefit


@admin.register(Benefit)
class BenefitAdmin(admin.ModelAdmin):
    list_display = ('text', 'beneficial_to', 'preview')
    empty_value_display = EMPTY_VALUE_ADMIN_PANEL
    list_filter = ('beneficial_to',)
    search_fields = ('text',)
    readonly_fields = ('preview',)

    def preview(self, obj):
        if obj.image:
            image = get_thumbnail(
                obj.image, '200x200', upscale=False, crop=False, quality=100
            )
            return format_html(
                f'<img src="{image.url}" '
                f'width="{image.width}" height="{image.height}">'
            )
        return ''
    preview.allow_tags = True
    preview.short_description = 'Предпросмотр загруженной фотографии'
