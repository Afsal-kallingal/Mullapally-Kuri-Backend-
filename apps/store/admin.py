from django.contrib import admin
from apps.product.models import *



# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('id','name','description','price','cost','profit','taxable_amount','discount_price','stock','product_category','brand','supplier','points','date_added', 'creator','image','updated_at',
#     )
# admin.site.register(Product,ProductAdmin)

# class SupplierAdmin(admin.ModelAdmin):
#     list_display = ('id','name','contact_email')
# admin.site.register(Supplier,SupplierAdmin)

# class ProductBrandAdmin(admin.ModelAdmin):
#     list_display = ('id','name')
# admin.site.register(ProductBrand,ProductBrandAdmin)

# class ProductCategoryAdmin(admin.ModelAdmin):
#     list_display = ('id','name')
# admin.site.register(ProductCategory,ProductCategoryAdmin)
