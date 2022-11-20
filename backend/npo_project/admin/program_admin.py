from django.contrib import admin

from ..models import Program, ProgramCharacteristic


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'location', 'image',)


@admin.register(ProgramCharacteristic)
class ProgramCharacteristicAdmin(admin.ModelAdmin):
    list_display = ('text',)
