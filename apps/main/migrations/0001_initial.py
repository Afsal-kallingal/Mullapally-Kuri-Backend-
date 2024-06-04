# Generated by Django 5.0.6 on 2024-05-17 09:29

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CronjobCall",
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
                ("date_added", models.DateTimeField(auto_now_add=True)),
                ("title", models.CharField(default="None", max_length=128)),
            ],
            options={
                "verbose_name": "CronjobCall",
                "verbose_name_plural": "CronjobCalls",
                "db_table": "main_CronjobCall",
                "ordering": ("-date_added",),
            },
        ),
    ]
