from django.contrib import admin
from .models import *


# Custom admin classes
class VolcanoAdmin(admin.ModelAdmin):
    list_display = ('Volcano_ID', 'Volcano_Name', 'Volcano_Type', 'Country', 'epoch_period', 'quantity', 'price')
    search_fields = ('Volcano_Name', 'Country', 'Volcano_Type')
    list_filter = ('Country', 'Volcano_Type')


admin.site.register(Volcano, VolcanoAdmin)





'''
from django.contrib import admin
from .models import *
from accounts.models import Customer  # Import Customer from accounts app



# Custom admin classes
class VolcanoAdmin(admin.ModelAdmin):
    list_display = ('Volcano_ID', 'Volcano_Name', 'Volcano_Type', 'Country', 'epoch_period', 'quantity', 'price')
    search_fields = ('Volcano_Name', 'Country', 'Volcano_Type')
    list_filter = ('Country', 'Volcano_Type')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'Customer', 'date_ordered', 'complete')
    list_filter = ('complete',)
    search_fields = ('Customer__name',)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('volcano_name', 'order_id', 'quantity', 'date_added')

    # Add these methods to display the volcano name and order id
    def volcano_name(self, obj):
        return obj.volcano.Volcano_Name

    def order_id(self, obj):
        return obj.order.id

class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('customer', 'order', 'address', 'city', 'state', 'zipcode', 'date_added')
    search_fields = ('customer__name', 'address')

# Register your models here.
admin.site.register(Volcano, VolcanoAdmin)
admin.site.register(Customer, CustomerAdmin)  # Register Customer without a custom admin class
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)
'''