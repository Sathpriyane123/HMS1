# Generated by Django 5.0 on 2024-01-20 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0018_delete_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Others')], max_length=10)),
                ('age', models.IntegerField()),
                ('place', models.CharField(max_length=100)),
                ('phonenumber', models.IntegerField()),
                ('bookingdate', models.DateField(max_length=10)),
                ('op', models.CharField(choices=[('general', 'General'), ('ent', 'ENT'), ('orthology', 'Orthology'), ('gynacology', 'Gynacology'), ('dental clinics', 'Dental Clinics'), ('psycology', 'Psycology'), ('pediatric clinics', 'Pediatric Clinics'), ('ophthalmology', 'Ophthalmology'), ('allergy clinics', 'Allergy Clinics'), ('neurology', 'Neurology')], max_length=100)),
                ('status', models.CharField(choices=[('booked', 'Booked'), ('postponed', 'Postponed'), ('confirmed', 'Confirmed'), ('checked', 'Checked'), ('cancelled', 'Cancelled')], max_length=100)),
            ],
        ),
    ]