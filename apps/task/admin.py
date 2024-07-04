# from django.contrib import admin
# from apps.target.models import *




# class TargetsAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'description', 'start_datetime', 'end_datetime', 
#                     'target_amount', 'achieved_amount', 'user', 'customer', 'get_products', 'status')

#     def get_products(self, obj):
#         return ", ".join([product.name for product in obj.products.all()])

#     get_products.short_description = 'Products'

# admin.site.register(Target, TargetsAdmin)

