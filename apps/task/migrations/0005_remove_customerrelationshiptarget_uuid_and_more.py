# Generated by Django 5.0.1 on 2024-07-04 11:39

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("task", "0004_alter_salesmansalestargetstatus_sales_target"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customerrelationshiptarget",
            name="uuid",
        ),
        migrations.RemoveField(
            model_name="salesmancustomerrelationshiptargetstatus",
            name="uuid",
        ),
        migrations.RemoveField(
            model_name="salesmantaskstatus",
            name="uuid",
        ),
        migrations.RemoveField(
            model_name="stafftask",
            name="uuid",
        ),
        migrations.AlterField(
            model_name="customerrelationshiptarget",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="salesmancustomerrelationshiptargetstatus",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="salesmantaskstatus",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="stafftask",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
        migrations.DeleteModel(
            name="SalesTarget",
        ),
    ]
