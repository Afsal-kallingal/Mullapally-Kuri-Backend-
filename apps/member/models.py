from django.db import models
from apps.user_account.models import User
from apps.main.models import BaseModel

class Member(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    nominee_full_name = models.CharField(max_length=255, blank=True, null=True)
    nominee_relation = models.CharField(max_length=100, blank=True, null=True)
    nominee_phone = models.CharField(max_length=15, blank=True, null=True)
    address_line1 = models.CharField(max_length=255, blank=True, null=True)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, default='India')  
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    dob = models.DateField(null=True, blank=True)  # Date of birth
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=True, null=True) 

    def __str__(self):
        return self.user.full_name


class Payment(BaseModel):
    PAYMENT_METHODS = [
        ('cash', 'Cash'),
        ('bank_transfer', 'Bank Transfer'),
        ('credit_card', 'Credit Card'),
        ('upi', 'UPI'),
        ('other', 'Other'),
    ]

    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS, default='cash') 
    notes = models.TextField(null=True, blank=True)  
    
    def __str__(self):
        return self.member.full_name
