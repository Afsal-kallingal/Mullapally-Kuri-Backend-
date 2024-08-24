# Generated by Django 5.0.6 on 2024-07-08 11:51

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Country",
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
                ("auto_id", models.IntegerField(db_index=True, unique=True)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                ("is_deleted", models.BooleanField(default=False)),
                ("name", models.CharField(max_length=100)),
                (
                    "creator",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Customer",
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
                ("auto_id", models.IntegerField(db_index=True, unique=True)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                ("is_deleted", models.BooleanField(default=False)),
                ("full_name", models.CharField(blank=True, max_length=255)),
                ("email", models.EmailField(blank=True, max_length=25, null=True)),
                ("phone", models.CharField(max_length=25, unique=True)),
                ("phone_number2", models.CharField(max_length=25, unique=True)),
                ("billing_address", models.TextField(blank=True, null=True)),
                ("shipping_address", models.TextField(blank=True, null=True)),
                (
                    "customer_type",
                    models.CharField(
                        choices=[
                            ("Individual", "Individual"),
                            ("Business", "Business"),
                        ],
                        default="Individual",
                        max_length=20,
                    ),
                ),
                ("tax_id", models.CharField(blank=True, max_length=20, null=True)),
                ("notes", models.TextField(blank=True, null=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "creator",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Department",
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
                ("auto_id", models.IntegerField(db_index=True, unique=True)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                ("is_deleted", models.BooleanField(default=False)),
                ("name", models.CharField(max_length=100, unique=True)),
                (
                    "creator",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Designation",
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
                ("auto_id", models.IntegerField(db_index=True, unique=True)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                ("is_deleted", models.BooleanField(default=False)),
                ("name", models.CharField(max_length=125, unique=True)),
                (
                    "creator",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="OfficeLocation",
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
                ("auto_id", models.IntegerField(db_index=True, unique=True)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                ("is_deleted", models.BooleanField(default=False)),
                ("address", models.CharField(max_length=255, unique=True)),
                (
                    "creator",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Site",
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
                ("auto_id", models.IntegerField(db_index=True, unique=True)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                ("is_deleted", models.BooleanField(default=False)),
                ("name", models.CharField(max_length=100)),
                (
                    "creator",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="State",
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
                ("auto_id", models.IntegerField(db_index=True, unique=True)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                ("is_deleted", models.BooleanField(default=False)),
                ("name", models.CharField(max_length=100)),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="states",
                        to="staff.country",
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="District",
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
                ("auto_id", models.IntegerField(db_index=True, unique=True)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                ("is_deleted", models.BooleanField(default=False)),
                ("name", models.CharField(max_length=100)),
                (
                    "creator",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "state",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="districts",
                        to="staff.state",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="WorkRole",
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
                ("auto_id", models.IntegerField(db_index=True, unique=True)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                ("is_deleted", models.BooleanField(default=False)),
                ("name", models.CharField(max_length=100, unique=True)),
                (
                    "creator",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Staff",
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
                ("auto_id", models.IntegerField(db_index=True, unique=True)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                ("is_deleted", models.BooleanField(default=False)),
                ("full_name", models.CharField(blank=True, max_length=255)),
                (
                    "address_line",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("dob", models.DateField(blank=True, default=None, null=True)),
                (
                    "salary",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                (
                    "rewards",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "operating",
                    models.CharField(
                        choices=[("office", "In Office"), ("field", "Field")],
                        max_length=10,
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="staff.department",
                    ),
                ),
                (
                    "designation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="staff.designation",
                    ),
                ),
                (
                    "district",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="investor_district",
                        to="staff.district",
                    ),
                ),
                (
                    "office_location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="staff.officelocation",
                    ),
                ),
                (
                    "site",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="staff.site"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="staff.workrole"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
