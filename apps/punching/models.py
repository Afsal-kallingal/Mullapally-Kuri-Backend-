from django.db import models
from apps.main.models import BaseModel
from apps.user_account.models import User
from django.utils import timezone


class Attendance(BaseModel):
    PUNCH_TYPE_CHOICES = [
        ('ESSL', 'Employee Self Service'),
        ('MANUAL', 'Manual')
    ]

    user = models.ForeignKey(User, related_name='attendances', on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    time_in = models.DateTimeField(null=True, blank=True)
    time_out = models.DateTimeField(null=True, blank=True)
    punch_type = models.CharField(max_length=10, choices=PUNCH_TYPE_CHOICES, default='ESSL')
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Attendance'
        verbose_name_plural = 'Attendances'
        unique_together = ('user', 'date_added')

    def __str__(self):
        return f"{self.user.username} - {self.date_added}"