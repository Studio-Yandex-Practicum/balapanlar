from django.contrib import admin
from django.utils.safestring import mark_safe

from balapanlar.settings import EMPTY_VALUE_ADMIN_PANEL
from ..models import Principle


@admin.register(Principle)
class PrinciplesAdmin(admin.ModelAdmin):
    fields = ('text', 'image', 'picture')
    list_display = ('text', 'picture')
    search_fields = ('text',)
    list_filter = ('text',)
    empty_value_display = EMPTY_VALUE_ADMIN_PANEL
    readonly_fields = ('picture',)

    def picture(self, obj):
        if obj.image != '':
            return mark_safe(
                f'<img src="{obj.image.url}" style="max-height: 100px;">')
        return 'Картинка ещё не сохранена'
    picture.short_description = 'Предпросмотр картинки'
