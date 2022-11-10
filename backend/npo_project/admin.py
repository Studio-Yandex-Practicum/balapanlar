from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import (Partners, Principles, Requisites)


admin.AdminSite.site_header = 'Администрирование - Балапанлар'


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


@admin.register(Requisites)
class RequisitesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'text',
    )
    list_editable = ('text',)
