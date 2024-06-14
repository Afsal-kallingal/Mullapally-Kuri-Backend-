from django.db import models
from apps.main.models import BaseModel
from apps.user_account.models import User
from apps.product.models import Product
from django.utils import timezone


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

    def __str__(self):
        return self.first_name
    
class Target(BaseModel):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),
    )
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    achieved_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='targetsS')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='targets')  
    products = models.ManyToManyField(Product, related_name='targets', blank=True)  # Many-to-Many relationship with Product
    # status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return self.name
  
    # def update_status(self):
    #     now = timezone.now()
    #     if now < self.start_datetime:
    #         self.status = 'Pending'
    #     elif self.start_datetime <= now <= self.end_datetime:
    #         self.status = 'Ongoing'
    #     elif self.achieved_amount >= self.target_amount:
    #         self.status = 'Completed'
    #     elif now > self.end_datetime and self.achieved_amount < self.target_amount:
    #         self.status = 'Failed'
    #     self.save()

    # def save(self, *args, **kwargs):
    #     self.update_status()
    #     super().save(*args, **kwargs)
     