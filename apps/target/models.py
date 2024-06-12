from django.db import models
from apps.main.models import BaseModel
from apps.user_account.models import User
from apps.product.models import Product


class Customer(BaseModel):
    CUSTOMER_TYPES = (
        ('Individual', 'Individual'),
        ('Business', 'Business'),
    )

    first_name = models.CharField(max_length=50,blank=True, null=True)
    last_name = models.CharField(max_length=50,blank=True, null=True)
    email = models.EmailField(max_length=25,blank=True, null=True)
    phone = models.CharField(max_length=25,unique=True)
    billing_address = models.TextField(blank=True, null=True)
    shipping_address = models.TextField(blank=True, null=True)
    customer_type = models.CharField(max_length=20, choices=CUSTOMER_TYPES, default='Individual')
    tax_id = models.CharField(max_length=20, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    customer_id = models.CharField(max_length=20,blank=True, null=True)

class Target(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    achieved_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='targets')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='targets')  
    products = models.ManyToManyField(Product, related_name='targets', blank=True)  # Many-to-Many relationship with Product

    def __str__(self):
        return self.name