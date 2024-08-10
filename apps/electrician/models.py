from django.db import models
from apps.main.models import BaseModel
from apps.user_account.models import User
from apps.staff.models import District

class Electrician(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")

    # Personal Details
    address_line = models.CharField(max_length=255, blank=True, null=True)
    temporary_address_line = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(null=True, blank=True, default=None)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True, related_name='electrician_district')
    # salary = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    national_id = models.CharField(max_length=20, blank=True, null=True)
    blood_group = models.CharField(max_length=3, blank=True, null=True)
    emergency_contact_name = models.CharField(max_length=50, blank=True, null=True)
    emergency_contact_number = models.CharField(max_length=15, blank=True, null=True)
    health_conditions = models.TextField(blank=True, null=True)

    # Marital Status
    MARITAL_STATUS_CHOICES = [
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorced', 'Divorced'),
        ('widowed', 'Widowed'),
    ]
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES, blank=True, null=True)

    # Spouse Details (conditionally collected if married)
    spouse_name = models.CharField(max_length=50, blank=True, null=True)
    spouse_dob = models.DateField(null=True, blank=True, default=None)
    spouse_occupation = models.CharField(max_length=50, blank=True, null=True)

    # Parent Details
    father_name = models.CharField(max_length=50, blank=True, null=True)
    mother_name = models.CharField(max_length=50, blank=True, null=True)

    # Professional Details
    years_of_experience = models.PositiveIntegerField(default=0, null=True, blank=True)
    certifications = models.TextField(blank=True, null=True)
    specialization = models.CharField(max_length=100, blank=True, null=True)
    previous_employers = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)

    # Nominee Details
    nominee_name = models.CharField(max_length=50, blank=True, null=True)
    nominee_relation = models.CharField(max_length=50, blank=True, null=True)
    nominee_dob = models.DateField(null=True, blank=True, default=None)
    nominee_contact_number = models.CharField(max_length=15, blank=True, null=True)
    nominee_address = models.CharField(max_length=100, blank=True, null=True)

    # Children Details (up to 5 children)
    child1_name = models.CharField(max_length=50, blank=True, null=True)
    child1_dob = models.DateField(null=True, blank=True, default=None)
    child1_gender = models.CharField(max_length=10, blank=True, null=True)
    child1_school = models.CharField(max_length=100, blank=True, null=True)
    
    child2_name = models.CharField(max_length=50, blank=True, null=True)
    child2_dob = models.DateField(null=True, blank=True, default=None)
    child2_gender = models.CharField(max_length=10, blank=True, null=True)
    child2_school = models.CharField(max_length=100, blank=True, null=True)
    
    child3_name = models.CharField(max_length=50, blank=True, null=True)
    child3_dob = models.DateField(null=True, blank=True, default=None)
    child3_gender = models.CharField(max_length=10, blank=True, null=True)
    child3_school = models.CharField(max_length=100, blank=True, null=True)
    
    child4_name = models.CharField(max_length=50, blank=True, null=True)
    child4_dob = models.DateField(null=True, blank=True, default=None)
    child4_gender = models.CharField(max_length=10, blank=True, null=True)
    child4_school = models.CharField(max_length=100, blank=True, null=True)
    
    child5_name = models.CharField(max_length=50, blank=True, null=True)
    child5_dob = models.DateField(null=True, blank=True, default=None)
    child5_gender = models.CharField(max_length=10, blank=True, null=True)
    child5_school = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.full_name

class ElectricianStaff(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    electrician = models.ForeignKey(Electrician, on_delete=models.CASCADE, related_name="electrician_staffs")
    # Personal Details
    address_line = models.CharField(max_length=255, blank=True, null=True)
    temporary_address_line = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(null=True, blank=True, default=None)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True, related_name='electrician_staff_district')
    # salary = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    national_id = models.CharField(max_length=20, blank=True, null=True)
    blood_group = models.CharField(max_length=3, blank=True, null=True)
    emergency_contact_name = models.CharField(max_length=50, blank=True, null=True)
    emergency_contact_number = models.CharField(max_length=15, blank=True, null=True)
    health_conditions = models.TextField(blank=True, null=True)

    # Marital Status
    MARITAL_STATUS_CHOICES = [
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorced', 'Divorced'),
        ('widowed', 'Widowed'),
    ]
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES, blank=True, null=True)

    # Spouse Details (conditionally collected if married)
    spouse_name = models.CharField(max_length=50, blank=True, null=True)
    spouse_dob = models.DateField(null=True, blank=True, default=None)
    spouse_occupation = models.CharField(max_length=50, blank=True, null=True)

    # Parent Details
    father_name = models.CharField(max_length=50, blank=True, null=True)
    mother_name = models.CharField(max_length=50, blank=True, null=True)

    # Professional Details
    years_of_experience = models.PositiveIntegerField(default=0, null=True, blank=True)
    certifications = models.TextField(blank=True, null=True)
    specialization = models.CharField(max_length=100, blank=True, null=True)
    previous_employers = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)

    # Nominee Details
    nominee_name = models.CharField(max_length=50, blank=True, null=True)
    nominee_relation = models.CharField(max_length=50, blank=True, null=True)
    nominee_dob = models.DateField(null=True, blank=True, default=None)
    nominee_contact_number = models.CharField(max_length=15, blank=True, null=True)
    nominee_address = models.CharField(max_length=100, blank=True, null=True)

    # Children Details (up to 5 children)
    child1_name = models.CharField(max_length=50, blank=True, null=True)
    child1_dob = models.DateField(null=True, blank=True, default=None)
    child1_gender = models.CharField(max_length=10, blank=True, null=True)
    child1_school = models.CharField(max_length=100, blank=True, null=True)
    
    child2_name = models.CharField(max_length=50, blank=True, null=True)
    child2_dob = models.DateField(null=True, blank=True, default=None)
    child2_gender = models.CharField(max_length=10, blank=True, null=True)
    child2_school = models.CharField(max_length=100, blank=True, null=True)
    
    child3_name = models.CharField(max_length=50, blank=True, null=True)
    child3_dob = models.DateField(null=True, blank=True, default=None)
    child3_gender = models.CharField(max_length=10, blank=True, null=True)
    child3_school = models.CharField(max_length=100, blank=True, null=True)
    
    child4_name = models.CharField(max_length=50, blank=True, null=True)
    child4_dob = models.DateField(null=True, blank=True, default=None)
    child4_gender = models.CharField(max_length=10, blank=True, null=True)
    child4_school = models.CharField(max_length=100, blank=True, null=True)
    
    child5_name = models.CharField(max_length=50, blank=True, null=True)
    child5_dob = models.DateField(null=True, blank=True, default=None)
    child5_gender = models.CharField(max_length=10, blank=True, null=True)
    child5_school = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.full_name

