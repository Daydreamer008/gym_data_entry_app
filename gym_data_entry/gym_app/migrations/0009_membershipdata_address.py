# Generated by Django 5.0 on 2023-12-13 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0008_dailyentry_address_dailyentry_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='membershipdata',
            name='address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
