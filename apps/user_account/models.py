from django.contrib.auth.models import PermissionsMixin,AbstractBaseUser,BaseUserManager
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
# from apps.main.models import BaseModel

import uuid
from django.apps import apps
from django.contrib import auth
# from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        GlobalUserModel = apps.get_model(self.model._meta.app_label, self.model._meta.object_name)
        username = GlobalUserModel.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)

    def with_perm(self, perm, is_active=True, include_superusers=True, backend=None, obj=None):
        if backend is None:
            backends = auth._get_backends(return_tuples=True)
            if len(backends) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError(
                    'You have multiple authentication backends configured and '
                    'therefore must provide the `backend` argument.'
                )
        elif not isinstance(backend, str):
            raise TypeError(
                'backend must be a dotted import path string (got %r).'
                % backend
            )
        else:
            backend = auth.load_backend(backend)
        if hasattr(backend, 'with_perm'):
            return backend.with_perm(
                perm,
                is_active=is_active,
                include_superusers=include_superusers,
                obj=obj,
            )
        return self.none()



# class BaseModel(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     auto_id = models.CharField(max_length=128,db_index = True,unique=True)
#     date_added = models.DateTimeField(auto_now_add=True)
#     is_deleted = models.BooleanField(default=False)
#     class Meta:
#         abstract = True


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    id =models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(unique=True,default=1,max_length=40)
    full_name = models.CharField(_("Name of User"), blank=True, max_length=255)
    dob = models.CharField(max_length=30,null=True,blank=True)
    country_code = models.CharField(max_length=5,null=True,blank=True,default=91)
    phone = models.CharField(max_length=30,unique=True)
    phone_verified = models.BooleanField(default=False)
    email = models.EmailField(_('email address'), null=True,blank=True)
    email_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    role = models.CharField(max_length=30,null=True,blank=True)
    is_admin = models.BooleanField(default=False,null=True,blank=True)
    is_superuser = models.BooleanField(default=False,null=True,blank=True)
    
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        swappable = 'AUTH_USER_MODEL'

    # def __str__(self):
    #     return str(self.get_username())
    def __str__(self):
        return self.full_name if self.full_name else self.get_username()
    
    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    # def get_full_name(self):
    #     """
    #     Return the first_name plus the last_name, with a space in between.
    #     """
    #     full_name = '%s %s' % (self.first_name, self.last_name)
    #     return full_name.strip()

    # def get_short_name(self):
    #     """Return the short name for the user."""
    #     return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    # @property
    # def is_staff(self):
    #     return self.staff

    # @property
    # def is_active(self):
    #     return self.active

    # @property
    # def is_admin(self):
    #     return self.admin

    # @property
    # def is_doctor(self):
    #     return self.doctor

    # @property
    # def is_user(self):
    #     return self.user
    
class LoginHistory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="+")
    login_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    ip_address = models.GenericIPAddressField()
    login_method = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'user_login_history'
        verbose_name = ('LoginHistory')
        verbose_name_plural = ('LoginHistories')
        ordering = ('-login_date',)
    def __str__(self):
        return str(self.user.full_name)
    



# class UserTransaction(models.Model):
#     PAYMENT_TYPES =(
#         ('debit', 'debit'),
#         ('credit', 'credit'),
#         )
#     PAYMENT_STATUS =(
#         ('pending', 'pending'),
#         ('created', 'created'),
#         ('captured', 'captured'),
#         ('cancelled', 'cancelled'),
#         ('late_authorized', 'late_authorized'),
#         ('success', 'success'),
#         ('failed', 'failed'),
#         )
#     name = models.CharField(max_length=128,null=True,blank=True,default="")
#     contact_number = models.CharField(max_length=128,null=True,blank=True,default="6235666630")
#     email = models.CharField(max_length=128,null=True,blank=True,default="info@khaf.in")
#     currency = models.CharField(null=True,blank=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="+")
#     payment_type = models.CharField(max_length=100,choices=PAYMENT_TYPES,null=True,blank=True,default='donation')
#     payment_status = models.CharField(max_length=100,choices=PAYMENT_STATUS,null=False,blank=False,default="created")
#     amount = models.DecimalField(max_digits=20, decimal_places=2,null=False,blank=False,default="0")
#     remark = models.TextField(null=True,blank=True)
#     trn_token = models.TextField(null=True,blank=True)

#     def __str__(self):
#         return str(self.user.full_name)

# @receiver(post_save,sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender,instance=None,created=False,**kwargs):
#     if created:
#         Token.objects.create(user=instance,key="58d727221227c48ce13a0507e994ef695c272a77") 