from django.contrib import admin

from ..models import Program, ProgramCharacteristic


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'description',
                    'location')
    list_editable = ('name', 'image', 'description',
                     'location',)


@admin.register(ProgramCharacteristic)
class ProgramCharacteristicAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_editable = ('text',)
