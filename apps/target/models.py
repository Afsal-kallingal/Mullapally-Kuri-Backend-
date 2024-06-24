from django.db import models
from apps.main.models import BaseModel
from apps.user_account.models import User
from apps.product.models import Product
from apps.staff.models import Staff

STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('approved', 'Approved'),
    ('rejected', 'Rejected'),
]

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
    # customer_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.first_name
    
# class Target(BaseModel):
#     STATUS_CHOICES = (
#         ('Pending', 'Pending'),
#         ('Ongoing', 'Ongoing'),
#         ('Completed', 'Completed'),
#         ('Failed', 'Failed'),
#     )
#     name = models.CharField(max_length=100)
#     description = models.TextField(null=True, blank=True)
#     start_datetime = models.DateTimeField()
#     end_datetime = models.DateTimeField()
#     target_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     achieved_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='targetsS')
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='targets')  
#     product =  models.ForeignKey(Product, on_delete=models.CASCADE , related_name='products')  
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

#     def __str__(self):
#         return self.name


class SalesTarget(BaseModel):
    salesman = models.ForeignKey(Staff, on_delete=models.CASCADE)
    # start_datetime = models.DateTimeField()
    period = models.DateTimeField()
    sales_target_revenue = models.DecimalField(max_digits=10, decimal_places=2,null=False,blank=False)
    units_sold_target = models.PositiveIntegerField()
    avg_transaction_value_target = models.DecimalField(max_digits=10, decimal_places=2,null=False,blank=False)
    description = models.TextField(blank=True)
    status = models.CharField(choices=STATUS_CHOICES, default='pending', max_length=20)
    reply = models.TextField(blank=True, null=True)

    def __str__(self):
        return {self.salesman.full_name} - {self.period}

class CustomerRelationshipTarget(BaseModel):
    salesman = models.ForeignKey(Staff, on_delete=models.CASCADE)
    period = models.DateField()
    customer_acquisition_target = models.PositiveIntegerField()
    customer_retention_target = models.DecimalField(max_digits=5, decimal_places=2)
    customer_satisfaction_score_target = models.DecimalField(max_digits=3, decimal_places=2)
    loyalty_program_signups_target = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    status = models.CharField(choices=STATUS_CHOICES, default='pending', max_length=20)
    reply = models.TextField(blank=True, null=True)

    def __str__(self):
        return {self.salesman.full_name} - {self.period}