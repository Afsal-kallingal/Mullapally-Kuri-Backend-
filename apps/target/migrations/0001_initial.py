# Generated by Django 5.0.1 on 2024-06-13 11:58

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("product", "0002_alter_product_cost_alter_product_description_and_more"),
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
                ("customer_id", models.CharField(blank=True, max_length=20, null=True)),
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
            name="Target",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
                ("start_datetime", models.DateTimeField()),
                ("end_datetime", models.DateTimeField()),
                ("target_amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "achieved_amount",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
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
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="targets",
                        to="target.customer",
                    ),
                ),
                (
                    "products",
                    models.ManyToManyField(
                        blank=True, related_name="targets", to="product.product"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="targets",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
