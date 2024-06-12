
from django.db import models
from apps.main.models import BaseModel


class ProductCategory(BaseModel):
    name = models.CharField(max_length=100)
    # parent_category = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='subcategories')

    def __str__(self):
        return self.name

class ProductBrand(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Supplier(BaseModel):
    name = models.CharField(max_length=100)
    contact_email = models.EmailField()

    def __str__(self):
        return self.name

class Product(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2 , default=0)
    cost = models.DecimalField(max_digits=10, decimal_places=2 ,default=0)  # Cost price
    profit = models.DecimalField(max_digits=10, decimal_places=2 ,default=0)  # Profit amount
    taxable_amount = models.DecimalField(max_digits=10, decimal_places=2 ,default=0)  # Taxable amount
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)  # Discounted price
    stock = models.IntegerField()
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)  # Loyalty points
    image = models.ImageField(upload_to='product_images', null=True, blank=True)  # Image field
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name