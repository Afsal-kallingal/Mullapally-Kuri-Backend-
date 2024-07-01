from django.db import models
from apps.main.models import BaseModel
from apps.user_account.models import User
from django.utils import timezone

class SalesTarget(BaseModel):
    salesman = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sales_targets')
    target_name = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField()
    sales_target_revenue = models.DecimalField(max_digits=10, decimal_places=2)
    units_sold_target = models.PositiveIntegerField()
    avg_transaction_value_target = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    target_period = models.CharField(max_length=50, null=True, blank=True)  # e.g., "Q1 2024", "2024-07", "H1 2024"
    progress = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)  # percentage of progress
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.salesman.get_full_name()} - {self.target_name} - {self.target_period}"

    def get_due_datetime(self):
        return timezone.make_aware(self.due_date)
    
class SalesmanSalesTargetStatus(BaseModel):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    sales_target = models.ForeignKey(SalesTarget, on_delete=models.CASCADE, related_name='target_statuses')
    completion_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, default='pending', max_length=20)
    notes = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sales_target.salesman.get_full_name()} - {self.sales_target.target_name} - {self.status} - {self.last_updated}"

    def mark_completed(self):
        self.status = 'completed'
        self.completion_date = timezone.now()
        self.save()

class CustomerRelationshipTarget(BaseModel):

    salesman = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_relationship_targets')
    target_name = models.CharField(max_length=50,null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(null=True, blank=True)
    # completion_date = models.DateTimeField(null=True, blank=True)
    target_period = models.CharField(max_length=50,null=True, blank=True)  # e.g., "Q1 2024", "2024-07", "H1 2024"
    customer_acquisition_target = models.PositiveIntegerField()
    customer_retention_target = models.DecimalField(max_digits=5, decimal_places=2)
    customer_satisfaction_score_target = models.DecimalField(max_digits=3, decimal_places=2)
    loyalty_program_signups_target = models.PositiveIntegerField()
    progress = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)  # percentage of progress
    description = models.TextField(blank=True)
    # status = models.CharField(choices=STATUS_CHOICES, default='pending', max_length=20)
    # reply = models.TextField(blank=True, null=True)
    # notes = models.TextField(blank=True, null=True)
    # last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return {self.salesman.get_full_name()} - {self.target_period}

    def get_due_datetime(self):
        return timezone.make_aware(self.due_date)

    # def mark_completed(self):
    #     self.status = 'completed'
    #     self.completion_date = timezone.now()
    #     self.save()

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
        return f"{self.customer_relationship_target.salesman.get_full_name()} - {self.customer_relationship_target.target_name} - {self.status} - {self.last_updated}"

    def mark_completed(self):
        self.status = 'completed'
        self.completion_date = timezone.now()
        self.save()
    
class StaffTask(BaseModel):
    PRIORITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    )

    staff = models.ForeignKey(User, on_delete=models.CASCADE, related_name='staff_tasks')
    task_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    target_period = models.CharField(max_length=50, null=True, blank=True)  # e.g., "Q1 2024", "2024-07", "H1 2024"
    description = models.TextField(blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    priority = models.CharField(choices=PRIORITY_CHOICES, default='medium', max_length=10)

    def __str__(self):
        return f"{self.task_name} - {self.staff.get_full_name()}"

    def get_due_date(self):
        return timezone.make_aware(self.due_date) if self.due_date else None

class SalesmanTaskStatus(BaseModel):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    )

    task = models.ForeignKey(StaffTask, on_delete=models.CASCADE, related_name='task_statuses')
    status = models.CharField(choices=STATUS_CHOICES, default='pending', max_length=20)
    notes = models.TextField(blank=True, null=True)
    completion_date = models.DateTimeField(null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.task.task_name} - {self.status}"

    def mark_completed(self):
        self.status = 'completed'
        self.completion_date = timezone.now()
        self.save()