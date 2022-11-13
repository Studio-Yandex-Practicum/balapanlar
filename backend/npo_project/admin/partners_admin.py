from django.contrib import admin
from django.utils.safestring import mark_safe

from ..models import Partners

admin.AdminSite.site_header = 'Администрирование - Балапанлар'


@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'image', 'logotype', 'url')
    list_display = (
        'name',
        'description',
        'logotype',
        'url',
    )
    list_editable = ('description',)
    search_fields = ('name',)
    list_filter = ('name',)
    readonly_fields = ('logotype',)

    def logotype(self, obj):
        if obj.image != '':
            return mark_safe(
                f'<img src="{obj.image.url}" style="max-height: 100px;">')
        return 'Логотип ещё не сохранён'
    logotype.short_description = 'Предпросмотр логотипа'
