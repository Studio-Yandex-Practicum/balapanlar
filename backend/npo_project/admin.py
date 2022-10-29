from django.contrib import admin
from .models import FAQ, Location

class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer') 
    search_fields = ('question',)

admin.site.register(FAQ, FAQAdmin)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('adress', 'image') 
    search_fields = ('adress',) 

admin.site.register(Location, LocationAdmin)