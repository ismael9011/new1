# Generated by Django 4.2.3 on 2023-07-23 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0006_alter_properties_distance'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='property',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='newapp.properties'),
        ),
    ]
