import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.user_account.models import User


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auto_id = models.IntegerField(db_index = True,unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True,related_name="+")
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class CronjobCall(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=128,default="None")

    class Meta:
        db_table = 'main_CronjobCall'
        verbose_name = ('CronjobCall')
        verbose_name_plural = ('CronjobCalls')
        ordering = ('-date_added',)
    def __str__(self):
        return self.title


