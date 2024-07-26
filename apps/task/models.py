from django.db import models
from apps.user_account.models import User
from django.utils import timezone
import uuid
from apps.main.models import BaseModel

class SaleTarget(BaseModel):
    salesman = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sal_targets')
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
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sales_target.target_name
    def mark_completed(self):
        self.status = 'completed'
        self.completion_date = timezone.now()
        self.save()

class CustomerRelationshipTarget(BaseModel):
    salesman = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_relationship_targets')
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

    staff = models.ForeignKey(User, on_delete=models.CASCADE, related_name='staff_tasks')
    task_name = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    target_period = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    priority = models.CharField(choices=PRIORITY_CHOICES, default='medium', max_length=10)
    audio = models.FileField(upload_to='task_audio/', null=True, blank=True)
    image = models.ImageField(upload_to='task_images/', null=True, blank=True)
    document = models.FileField(upload_to='task_documents/', null=True, blank=True)
    contact_file = models.FileField(upload_to='task_contacts/', null=True, blank=True)

    def __str__(self):
        return self.task_name

    def get_due_date(self):
        return timezone.make_aware(self.due_date) if self.due_date else None
    
    # def task_history(self,staff):
    #     # Create a task history entry
    #     TaskHistory.objects.create(
    #         task=self,
    #         changed_by=staff,
    #     )

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


# class TaskHistory(models.Model):
#     task = models.ForeignKey(StaffTask, on_delete=models.CASCADE, related_name='history')
#     changed_by = models.ForeignKey(User, on_delete=models.CASCADE)
#     change_date = models.DateTimeField(auto_now_add=True)
#     change_description = models.TextField(null=True,blank=True)

#     def __str__(self):
#         return f"{self.task.task_name} changed by {self.changed_by.username}"

class CompanyNotes(BaseModel):
    note_title = models.CharField(max_length=55, null=True, blank=True)
    note = models.TextField(blank=True, null=True)
    audio = models.FileField(upload_to='company_notes_audio/', null=True, blank=True)
    image = models.ImageField(upload_to='company_notes_images/', null=True, blank=True)

    def __str__(self):
        return self.note[:50] if self.note else 'No Note'

