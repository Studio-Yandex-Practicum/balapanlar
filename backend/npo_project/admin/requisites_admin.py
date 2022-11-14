from django.contrib import admin

from ..models import Requisites


@admin.register(Requisites)
class RequisitesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'text',
    )
    list_editable = ('text',)
