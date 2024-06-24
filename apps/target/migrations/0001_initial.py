# Generated by Django 5.0.1 on 2024-06-24 14:50

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("staff", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
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
                ("auto_id", models.PositiveIntegerField(db_index=True, unique=True)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                ("is_deleted", models.BooleanField(default=False)),
                ("first_name", models.CharField(blank=True, max_length=50, null=True)),
                ("last_name", models.CharField(blank=True, max_length=50, null=True)),
                ("email", models.EmailField(blank=True, max_length=25, null=True)),
                ("phone", models.CharField(max_length=25, unique=True)),
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
                        default=1,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="CustomerRelationshipTarget",
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
                ("auto_id", models.PositiveIntegerField(db_index=True, unique=True)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                ("is_deleted", models.BooleanField(default=False)),
                ("period", models.DateField()),
                ("customer_acquisition_target", models.PositiveIntegerField()),
                (
                    "customer_retention_target",
                    models.DecimalField(decimal_places=2, max_digits=5),
                ),
                (
                    "customer_satisfaction_score_target",
                    models.DecimalField(decimal_places=2, max_digits=3),
                ),
                ("loyalty_program_signups_target", models.PositiveIntegerField()),
                ("description", models.TextField(blank=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("approved", "Approved"),
                            ("rejected", "Rejected"),
                        ],
                        default="pending",
                        max_length=20,
                    ),
                ),
                ("reply", models.TextField(blank=True, null=True)),
                (
                    "creator",
                    models.ForeignKey(
                        blank=True,
                        default=1,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "salesman",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="staff.staff"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SalesTarget",
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
                ("auto_id", models.PositiveIntegerField(db_index=True, unique=True)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                ("is_deleted", models.BooleanField(default=False)),
                ("period", models.DateTimeField()),
                (
                    "sales_target_revenue",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("units_sold_target", models.PositiveIntegerField()),
                (
                    "avg_transaction_value_target",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("description", models.TextField(blank=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("approved", "Approved"),
                            ("rejected", "Rejected"),
                        ],
                        default="pending",
                        max_length=20,
                    ),
                ),
                ("reply", models.TextField(blank=True, null=True)),
                (
                    "creator",
                    models.ForeignKey(
                        blank=True,
                        default=1,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "salesman",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="staff.staff"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
