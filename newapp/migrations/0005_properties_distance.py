# Generated by Django 4.2.3 on 2023-07-23 21:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("newapp", "0004_properties_address_properties_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="properties",
            name="distance",
            field=models.IntegerField(default=10),
        ),
    ]
