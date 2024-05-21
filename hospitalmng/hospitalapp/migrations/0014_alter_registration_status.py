# Generated by Django 5.0 on 2024-01-08 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0013_remove_registration_details_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='status',
            field=models.CharField(choices=[('emergency', 'Emergency'), ('waiting', 'Wating'), ('checking', 'Checking'), ('checked', 'Checked')], max_length=100),
        ),
    ]