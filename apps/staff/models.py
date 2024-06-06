from django.db import models
from apps.user_account.models import User
# from apps.course import models as course_models
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
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name

class Work_Role(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Department(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class OfficeLocation(BaseModel):
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.address

class Site(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Report_To(BaseModel):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="+")

    def __str__(self):
        return self.name

class Staff(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="+")
    OPERATING_CHOICES = [
        ('office', 'In Office'),
        ('field', 'Field'),
    ]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30,blank=True, null=True)
    email = models.EmailField(blank=True, null=True,default='')
    country_code = models.CharField(max_length=5,default=91)
    phone_number = models.CharField(max_length=15,unique=True)
    address_line = models.CharField(max_length=255,blank=True, null=True)
    dob = models.DateField(null=True, blank=True,default='')
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True,related_name='investor_district')
    salary = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    rewards = models.DecimalField(max_digits=10, decimal_places=2 ,blank=True, null=True)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    post = models.ForeignKey(Work_Role, on_delete=models.CASCADE)
    reports_to = models.ForeignKey(Report_To ,on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)  
    office_location = models.ForeignKey(OfficeLocation, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    operating = models.CharField(max_length=10, choices=OPERATING_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"