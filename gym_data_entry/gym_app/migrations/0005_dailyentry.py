# Generated by Django 5.0 on 2023-12-06 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0004_membershipdata_delete_membership_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
