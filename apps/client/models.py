from django.db import models
from apps.main.models import BaseModel
from apps.user_account.models import User
from apps.staff.models import District,Staff
from apps.electrician.models import Electrician

class Client(BaseModel):
    CLIENT_TYPE_CHOICES = [
        ('end_user', 'End User'),
        ('business_client', 'Business Client'),
        ('government', 'Government'),
        ('non_profit', 'Non-Profit'),
    ]

    # Personal Details
    full_name = models.CharField(max_length=100, blank=True, null=True)
    address_line = models.CharField(max_length=225, blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True, related_name='client_district_name')

    postal_code = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    emergency_phone = models.CharField(max_length=20, blank=True, null=True)
    gst_number = models.CharField(max_length=20, blank=True, null=True)
    client_type = models.CharField(max_length=20, choices=CLIENT_TYPE_CHOICES, blank=True, null=True)

    # Professional Details
    company_name = models.CharField(max_length=100, blank=True, null=True)
    job_title = models.CharField(max_length=50, blank=True, null=True)
    industry = models.CharField(max_length=50, blank=True, null=True)

    # Follow-up Details
    followup_date = models.DateField(null=True, blank=True)
    followup_time = models.TimeField(null=True, blank=True)
    notes = models.TextField(blank=True, null=True)

    # Location Details
    latitude = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
    google_maps_url = models.URLField(blank=True, null=True)

    # Assigned User
    assigned_user = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True, related_name='client_assigned_staff')

    # Profile Photo
    profile_photo = models.ImageField(upload_to='client_photos/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.latitude is not None and self.longitude is not None:
            self.google_maps_url = f'https://www.google.com/maps?q={self.latitude},{self.longitude}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.full_name or "Unnamed Client"} - {self.company_name or ""}'

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

class ClientInteraction(BaseModel):
    INTERACTION_TYPE_CHOICES = [
        ('call', 'Call'),
        ('email', 'Email'),
        ('meeting', 'Meeting'),
        ('complaint', 'Complaint'),
        ('support_request', 'Support Request'),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='interactions')
    interaction_type = models.CharField(max_length=20, choices=INTERACTION_TYPE_CHOICES)
    interaction_date = models.DateTimeField()
    staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True, related_name='client_interactions')
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.client.full_name} - {self.interaction_type} on {self.interaction_date}'

    class Meta:
        verbose_name = 'Client Interaction'
        verbose_name_plural = 'Client Interactions'
        ordering = ['-interaction_date']


class ServiceRequest(BaseModel):
    customer_name = models.CharField(max_length=100)
    customer_contact = models.CharField(max_length=15)
    customer_address = models.TextField()
    request_description = models.TextField()
    request_date = models.DateTimeField(auto_now_add=True)
    preferred_service_date = models.DateField(null=True, blank=True)

    # Status Choices
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed'),
    ]
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='open')

    # Priority Choices
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    ]
    priority = models.CharField(max_length=15, choices=PRIORITY_CHOICES, default='medium')

    # Location Sharing
    location_share_url = models.URLField(max_length=200, blank=True, null=True)

    # Follow-up
    followed_up_by = models.ForeignKey(Electrician, on_delete=models.SET_NULL, null=True, blank=True, related_name='service_requests_followed_up')
    follow_up_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Service Request from {self.customer_name} - {self.status}"

    class Meta:
        verbose_name = 'Service Request'
        verbose_name_plural = 'Service Requests'

