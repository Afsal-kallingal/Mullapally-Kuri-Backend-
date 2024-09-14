# Generated by Django 5.0.6 on 2024-09-14 18:13

import apps.user_account.models
import django.db.models.deletion
import django.utils.timezone
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("username", models.CharField(default=1, max_length=40, unique=True)),
                (
                    "full_name",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Name of User"
                    ),
                ),
                ("dob", models.CharField(blank=True, max_length=30, null=True)),
                (
                    "country_code",
                    models.CharField(blank=True, default=91, max_length=5, null=True),
                ),
                ("phone", models.CharField(max_length=30, unique=True)),
                ("phone_verified", models.BooleanField(default=False)),
                (
                    "email",
                    models.EmailField(
                        blank=True,
                        max_length=254,
                        null=True,
                        verbose_name="email address",
                    ),
                ),
                ("email_verified", models.BooleanField(default=False)),
                ("role", models.CharField(blank=True, max_length=30, null=True)),
                ("is_admin", models.BooleanField(blank=True, default=False, null=True)),
                (
                    "is_superuser",
                    models.BooleanField(blank=True, default=False, null=True),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "swappable": "AUTH_USER_MODEL",
            },
            managers=[
                ("objects", apps.user_account.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="LoginHistory",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("login_date", models.DateTimeField(auto_now_add=True, null=True)),
                ("ip_address", models.GenericIPAddressField()),
                ("login_method", models.CharField(max_length=100)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "LoginHistory",
                "verbose_name_plural": "LoginHistories",
                "db_table": "user_login_history",
                "ordering": ("-login_date",),
            },
        ),
    ]
