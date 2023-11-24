# Generated by Django 4.2.7 on 2023-11-24 06:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="messagemodel",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]
