from django.contrib import admin

from ..models import Program, ProgramCharacteristic


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'location', 'image',)
    list_editable = ('image', 'description', 'location',)


@admin.register(ProgramCharacteristic)
class ProgramCharacteristicAdmin(admin.ModelAdmin):
    list_display = ('text',)
