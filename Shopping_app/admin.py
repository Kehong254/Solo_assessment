from django.contrib import admin
from .models import Volcano, Cart, CartItem

class VolcanoAdmin(admin.ModelAdmin):
    list_display = ('Volcano_ID', 'Volcano_Name', 'Volcano_Type', 'Country', 'Latitude', 'Longitude', 'price', 'quantity')
    search_fields = ('Volcano_Name', 'Volcano_Type', 'Country')



admin.site.register(Volcano, VolcanoAdmin)

