# Generated by Django 5.0 on 2024-01-20 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0017_feedback'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Appointment',
        ),
    ]