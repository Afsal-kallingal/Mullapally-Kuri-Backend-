from django.db import models
from apps.user_account.models import User
from apps.main.models import BaseModel

class Country(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class State(BaseModel):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='states')

    def __str__(self):
        return self.name

class District(BaseModel):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='districts')

    def __str__(self):
        return self.name

class Designation(BaseModel):
    name = models.CharField(max_length=125,unique=True)

    def __str__(self):
        return self.name

class WorkRole(BaseModel):  
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class Department(BaseModel):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class OfficeLocation(BaseModel):
    address = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.address

class Site(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Staff(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    OPERATING_CHOICES = [
        ('office', 'In Office'),
        ('field', 'Field'),
    ]
    full_name = models.CharField(blank=True, max_length=255)
    # email = models.EmailField(blank=True, null=True, default='')/
    # country_code = models.CharField(max_length=5, default='91')
    # phone_number = models.CharField(max_length=15, unique=True)
    address_line = models.CharField(max_length=255, blank=True, null=True)
    dob = models.DateField(null=True, blank=True, default=None)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True, related_name='investor_district')
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    rewards = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    post = models.ForeignKey(WorkRole, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)  
    office_location = models.ForeignKey(OfficeLocation, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    operating = models.CharField(max_length=10, choices=OPERATING_CHOICES)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.full_name

class Customer(BaseModel):
    CUSTOMER_TYPES = (
        ('Individual', 'Individual'),
        ('Business', 'Business'),
    )

    full_name = models.CharField(blank=True, max_length=255)
    # last_name = models.CharField(max_length=50,blank=True, null=True)
    email = models.EmailField(max_length=25,blank=True, null=True)
    phone = models.CharField(max_length=25,unique=True)
    phone_number2 = models.CharField(max_length=25,unique=True)
    billing_address = models.TextField(blank=True, null=True)
    shipping_address = models.TextField(blank=True, null=True)
    customer_type = models.CharField(max_length=20, choices=CUSTOMER_TYPES, default='Individual')
    tax_id = models.CharField(max_length=20, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    # customer_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.first_name
    