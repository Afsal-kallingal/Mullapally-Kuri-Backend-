from django.db import models
from apps.user_account.models import User
from apps.staff.models import District
from apps.main.models import BaseModel

class Investor(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="investors")
    address_line1 = models.CharField(max_length=255, blank=True, null=True)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    post_office = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(null=True, blank=True, default='')
    certificate_number = models.CharField(max_length=50, unique=True, null=True, blank=True, default='')
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True, related_name='investor_districts')
    pincode = models.CharField(max_length=20, blank=True, null=True)
    share_number = models.CharField(max_length=50, blank=True, null=True)
    bank_holder_name = models.CharField(max_length=255, blank=True, null=True)
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    bank_branch = models.CharField(max_length=255, blank=True, null=True)
    bank_account_number = models.CharField(max_length=50, blank=True, null=True)
    bank_ifsc = models.CharField(max_length=20, blank=True, null=True)
    number_of_shares = models.PositiveIntegerField(default=0)
    rewards = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    dividend = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ID_PROOF_CHOICES = (
        ('adhar', 'Aadhar Card'),
        ('pan', 'PAN Card'),
    )
    id_proof_type = models.CharField(max_length=10, choices=ID_PROOF_CHOICES, blank=True, null=True)
    id_proof_number = models.CharField(max_length=50, blank=True, null=True)
    nominee_name = models.CharField(max_length=255, blank=True, null=True)
    nominee_address_line1 = models.CharField(max_length=255, blank=True, null=True)
    nominee_address_line2 = models.CharField(max_length=255, blank=True, null=True)
    nominee_postoffice = models.CharField(max_length=100, blank=True, null=True, default='')
    nominee_pincode = models.CharField(max_length=20, blank=True, null=True, default='')
    nominee_id_proof_type = models.CharField(max_length=10, choices=ID_PROOF_CHOICES, blank=True, null=True)
    nominee_id_proof_number = models.CharField(max_length=50, blank=True, null=True)
    nominee_mobile = models.CharField(max_length=20, blank=True, null=True)
    nominee_country_code = models.CharField(max_length=5, default='91')
    nominee_email = models.EmailField(blank=True, null=True)
    nominee_district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True, related_name='nominee_districts')

    class Meta:
        verbose_name = "Investor"
        verbose_name_plural = "Investors"

class Company(BaseModel):
    company_name = models.CharField(max_length=255, blank=True, null=True)
    company_description = models.TextField(blank=True, null=True)
    terms = models.TextField(blank=True, null=True)
    benefits = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.company_name
