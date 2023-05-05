from django.contrib import admin
from .models import Volcano, Cart, CartItem, Address

# Custom admin classes
class VolcanoAdmin(admin.ModelAdmin):
    list_display = ('Volcano_ID', 'Volcano_Name', 'Volcano_Type', 'Country', 'epoch_period', 'quantity', 'price')
    search_fields = ('Volcano_Name', 'Country', 'Volcano_Type')
    list_filter = ('Country', 'Volcano_Type')

class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'user', 'created_at', 'updated_at')
    search_fields = ('cart_id', 'user')
    list_filter = ('cart_id', 'user', 'created_at', 'updated_at')

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'volcano', 'quantity')

class AddressAdmin(admin.ModelAdmin):
    list_display = ('Address_id', 'user', 'line_1', 'line_2', 'country', 'postal_code', 'phone_number')
    list_filter = ('country',)
    search_fields = ('line_1', 'line_2', 'country', 'postal_code', 'phone_number')



admin.site.register(Address, AddressAdmin)


admin.site.register(Volcano, VolcanoAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
