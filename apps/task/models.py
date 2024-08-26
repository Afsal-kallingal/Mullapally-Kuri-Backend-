from django.db import models
from apps.staff.models import Staff
from apps.user_account.models import User
from django.utils import timezone
from apps.main.models import BaseModel
import uuid


class SaleTarget(BaseModel):
    salesman = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='sal_targets')
    target_name = models.CharField(max_length=50, null=True, blank=True)
    due_date = models.DateTimeField(null=True) 
    sales_target_revenue = models.DecimalField(max_digits=10, decimal_places=2)
    units_sold_target = models.CharField(max_length=50, null=True, blank=True)
    avg_transaction_value_target = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    target_period = models.CharField(max_length=50, null=True, blank=True)
    progress = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.target_name

    def get_due_datetime(self):
        return timezone.make_aware(self.due_date)

class SalesmanSalesTargetStatus(BaseModel):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    sales_target = models.ForeignKey(SaleTarget, on_delete=models.CASCADE, related_name='sales_target_status')
    completion_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, default='pending', max_length=20)
    notes = models.TextField(blank=True, null=True)
    progress_sale_revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sales_target.target_name
    def mark_completed(self):
        self.status = 'completed'
        self.completion_date = timezone.now()
        self.save()

class CustomerRelationshipTarget(BaseModel):
    salesman = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='customer_relationship_targets')
    target_name = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(null=True, blank=True)
    target_period = models.CharField(max_length=50, null=True, blank=True)
    customer_acquisition_target = models.PositiveIntegerField()
    customer_retention_target = models.DecimalField(max_digits=5, decimal_places=2)
    customer_satisfaction_score_target = models.DecimalField(max_digits=3, decimal_places=2)
    loyalty_program_signups_target = models.PositiveIntegerField()
    progress = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    description = models.TextField(blank=True)

    def __str__(self):
        # return {self.salesman.get_full_name()} - {self.target_period}
        return self.target_name

    def get_due_datetime(self):
        return timezone.make_aware(self.due_date)

class SalesmanCustomerRelationshipTargetStatus(BaseModel):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    customer_relationship_target = models.ForeignKey(CustomerRelationshipTarget, on_delete=models.CASCADE, related_name='relationship_target_statuses')
    completion_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, default='pending', max_length=20)
    notes = models.TextField(blank=True, null=True)
    progress_customer_satisfaction_score = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer_relationship_target.salesman.get_full_name()
    def mark_completed(self):
        self.status = 'completed'
        self.completion_date = timezone.now()
        self.save()

class StaffTask(BaseModel):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='staff_tasks')
    task_name = models.CharField(max_length=255, null=True, blank=True)
    target_period = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    priority = models.CharField(choices=PRIORITY_CHOICES, default='medium', max_length=10)
    document = models.FileField(upload_to='task_documents/', null=True, blank=True)
    contact_file = models.FileField(upload_to='task_contacts/', null=True, blank=True)
    # New image fields
    image_1 = models.ImageField(upload_to='task_images/', null=True, blank=True)
    image_2 = models.ImageField(upload_to='task_images/', null=True, blank=True)
    image_3 = models.ImageField(upload_to='task_images/', null=True, blank=True)
    image_4 = models.ImageField(upload_to='task_images/', null=True, blank=True)
    image_5 = models.ImageField(upload_to='task_images/', null=True, blank=True)
    image_6 = models.ImageField(upload_to='task_images/', null=True, blank=True)
    image_7 = models.ImageField(upload_to='task_images/', null=True, blank=True)
    image_8 = models.ImageField(upload_to='task_images/', null=True, blank=True)
    # New audio fields
    audio_1 = models.FileField(upload_to='task_audio/', null=True, blank=True)
    audio_2 = models.FileField(upload_to='task_audio/', null=True, blank=True)
    audio_3 = models.FileField(upload_to='task_audio/', null=True, blank=True)
    audio_4 = models.FileField(upload_to='task_audio/', null=True, blank=True)
    audio_5 = models.FileField(upload_to='task_audio/', null=True, blank=True)
    audio_6 = models.FileField(upload_to='task_audio/', null=True, blank=True)
    audio_7 = models.FileField(upload_to='task_audio/', null=True, blank=True)
    audio_8 = models.FileField(upload_to='task_audio/', null=True, blank=True)

    def __str__(self):
        return self.task_name

    def forward_task(self, new_staff):
        TaskHistory.objects.create(
            task=self,
            previous_staff=self.staff,
            new_staff=new_staff,
            forwarded_at=timezone.now()
        )
        self.staff = new_staff
        self.save()

class TaskHistory(models.Model):
    task = models.ForeignKey(StaffTask, on_delete=models.CASCADE, related_name='task_histories')
    previous_staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, related_name='previous_tasks')
    new_staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, related_name='new_tasks')
    forwarded_at = models.DateTimeField()

    def __str__(self):
        return f'Task {self.task.task_name} forwarded from {self.previous_staff} to {self.new_staff}'

class SalesmanTaskStatus(BaseModel):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    task = models.ForeignKey(StaffTask, on_delete=models.CASCADE, related_name='task_statuses')
    status = models.CharField(choices=STATUS_CHOICES, default='pending', max_length=20)
    notes = models.TextField(blank=True, null=True)
    completion_date = models.DateTimeField(null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task.task_name

    def mark_completed(self):
        self.status = 'completed'
        self.completion_date = timezone.now()
        self.save()

class CompanyNotes(BaseModel):
    note_title = models.CharField(max_length=55, null=True, blank=True)
    note = models.TextField(blank=True, null=True)
    audio = models.FileField(upload_to='company_notes_audio/', null=True, blank=True)
    image = models.ImageField(upload_to='company_notes_images/', null=True, blank=True)
    tags = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.note_title if self.note_title else (self.note[:50] if self.note else 'No Note')

    class Meta:
        verbose_name = 'Company Note'
        verbose_name_plural = 'Company Notes'

class DeliveryArea(BaseModel):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
    

class Delivery(BaseModel):
    # Delivery and Return types
    DELIVERY = 'DELIVERY'
    RETURN = 'RETURN'

    # Delivery Statuses
    PENDING = 'PENDING'
    ONGOING = 'ONGOING'
    COMPLETE = 'COMPLETE'

    # Payment Modes
    CASH = 'CASH'
    CHECK = 'CHECK'
    UPI = 'UPI'

    # Choices for fields
    DELIVERY_TYPE_CHOICES = [
        (DELIVERY, 'Delivery'),
        (RETURN, 'Return'),
    ]

    DELIVERY_STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (ONGOING, 'Ongoing'),
        (COMPLETE, 'Complete'),
    ]

    PAYMENT_MODE_CHOICES = [
        (CASH, 'Cash'),
        (CHECK, 'Check'),
        (UPI, 'UPI'),
    ]

    # Model Fields
    delivered_staff = models.ForeignKey(
        Staff, on_delete=models.SET_NULL, null=True, blank=True, related_name="delivery_staff"
    )
    heading = models.CharField(max_length=255)
    location_place_name = models.CharField(max_length=255)
    delivery_area = models.ForeignKey(
        DeliveryArea, on_delete=models.SET_NULL, null=True, blank=True
    )
    delivery_date = models.DateTimeField()
    delivery_type = models.CharField(max_length=10, choices=DELIVERY_TYPE_CHOICES)
    status = models.CharField(max_length=10, choices=DELIVERY_STATUS_CHOICES, default=PENDING)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Customer Fields
    customer_name = models.CharField(max_length=255)
    customer_address = models.TextField()
    customer_phone = models.CharField(max_length=20)

    # New Fields
    pending_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    payment_mode = models.CharField(max_length=10, choices=PAYMENT_MODE_CHOICES, null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    call_report_followup = models.TextField(null=True, blank=True)
    delivery_google_map_url = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.heading

    