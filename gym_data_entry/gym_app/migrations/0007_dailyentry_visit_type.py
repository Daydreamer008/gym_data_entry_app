# Generated by Django 5.0 on 2023-12-06 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0006_rename_create_time_dailyentry_entry_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyentry',
            name='visit_type',
            field=models.CharField(blank=True, choices=[('Regular', 'Regular'), ('Guest', 'Guest')], max_length=10, null=True),
        ),
    ]
