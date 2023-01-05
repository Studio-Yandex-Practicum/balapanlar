from django.contrib import admin
from django.utils.safestring import mark_safe

from ..models import Program, ProgramCharacteristic


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'location', 'image',
                    'image_preview')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image != '':
            return mark_safe(
                f'<img src="{obj.image.url}" style="max-height: 100px;">')
        return 'Картинка ещё не сохранена'
    image_preview.short_description = 'Предпросмотр картинки'


@admin.register(ProgramCharacteristic)
class ProgramCharacteristicAdmin(admin.ModelAdmin):
    list_display = ('text',)
