from django.contrib import admin
from apps.target.models import *



class CustomerAdmin(admin.ModelAdmin):
    list_display = ('auto_id', 'first_name', 'last_name', 'email', 'phone', 'billing_address',
            'shipping_address', 'customer_type', 'tax_id', 'notes', 'is_active',
    )
admin.site.register(Customer,CustomerAdmin)


# class TargetsAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'description', 'start_datetime', 'end_datetime', 
#                     'target_amount', 'achieved_amount', 'user', 'customer', 'get_products', 'status')

#     def get_products(self, obj):
#         return ", ".join([product.name for product in obj.products.all()])

#     get_products.short_description = 'Products'

# admin.site.register(Target, TargetsAdmin)

