from django.contrib import admin
from .models import *

# Custom admin classes
class VolcanoAdmin(admin.ModelAdmin):
    list_display = ('Volcano_ID', 'Volcano_Name', 'Volcano_Type', 'Country')
    search_fields = ('Volcano_Name', 'Country', 'Volcano_Type')
    list_filter = ('Country', 'Volcano_Type')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email')
    search_fields = ('name', 'email')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'Customer', 'date_ordered', 'complete')  # Changed 'data_ordered' to 'date_ordered'
    list_filter = ('complete',)
    search_fields = ('Customer__name',)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'order_id', 'quantity', 'date_added')  # Changed 'product' to 'product_name' and 'order' to 'order_id'
    search_fields = ('product__name',)

    # Add these methods to display the product name and order id
    def product_name(self, obj):
        return obj.product.name

    def order_id(self, obj):
        return obj.order.id


class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('customer', 'order', 'address', 'city', 'state', 'zipcode', 'date_added')
    search_fields = ('customer__name', 'address')

# Register your models here.
admin.site.register(Volcano, VolcanoAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)
