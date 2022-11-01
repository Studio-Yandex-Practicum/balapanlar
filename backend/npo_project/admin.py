from django.contrib import admin
from .models import FAQ, Location


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
    search_fields = ('question',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('adress', 'image')
    search_fields = ('adress',)
