from django.contrib import admin
from django.utils.safestring import mark_safe

from ..models import Principles


@admin.register(Principles)
class PrinciplesAdmin(admin.ModelAdmin):
    fields = ('text', 'image', 'picture')
    list_display = (
        'text',
        'picture',
    )
    search_fields = ('text',)
    list_filter = ('text',)
    empty_value_display = '-пусто-'
    readonly_fields = ('picture',)

    def picture(self, obj):
        if obj.image != '':
            return mark_safe(
                f'<img src="{obj.image.url}" style="max-height: 100px;">')
        return 'Картинка ещё не сохранена'
    picture.short_description = 'Предпросмотр картинки'
