from django.contrib import admin

from ..models import Requisite


@admin.register(Requisite)
class RequisitesAdmin(admin.ModelAdmin):
    list_display = ('text',)
    list_display_links = ('text',)
