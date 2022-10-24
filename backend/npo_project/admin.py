from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Partners, Principles


@admin.register(Principles)
class PrinciplesAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'comment',
    )
    search_fields = ('title',)
    list_filter = ('title',)    
    empty_value_display = '-пусто-'


@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    fields = ('name', 'text', 'image', 'logotype', 'url')
    list_display = (
        'name',
        'text',
        'logotype',
        'url',
    )
    list_editable = ('text',)
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'
    readonly_fields = ('logotype',)

    def logotype(self, obj):
        return mark_safe(
            f'<img src="{obj.image.url}" style="max-height: 100px;">')
