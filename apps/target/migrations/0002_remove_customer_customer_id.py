# Generated by Django 5.0.1 on 2024-06-21 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("target", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customer",
            name="customer_id",
        ),
    ]
