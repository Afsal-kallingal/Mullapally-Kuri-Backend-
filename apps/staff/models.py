from django.db import models
from apps.user_account.models import User
# from apps.course import models as course_models
from apps.main.models import BaseModel


class Staff(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    ROLE_CHOICES=(
        ('salesman', 'Salesman'),
        ('fieldsalesman', 'Field Salesman'),
        ('marketing', 'Marketing'),
        ('billing', 'Billing'),
        ('cashier', 'Cashier'),
        ('accountant', 'Accountant'),
        ('telecalling', 'Telecalling'),
        ('purchase', 'Purchase'),
        ('delivery', 'Delivery'),
        ('warehousing', 'Warehousing'),
    )
    role = models.CharField(max_length=50, choices=ROLE_CHOICES ,blank=True, null=True)
    sales_target = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"