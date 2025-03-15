# Generated by Django 5.0 on 2024-01-07 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0010_delete_doctors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctorsname', models.CharField(max_length=200)),
                ('op', models.CharField(choices=[('general', 'General'), ('ent', 'ENT'), ('orthology', 'Orthology'), ('gynacology', 'Gynacology'), ('dental clinics', 'Dental Clinics'), ('psycology', 'Psycology'), ('pediatric clinics', 'Pediatric Clinics'), ('ophthalmology', 'Ophthalmology'), ('allergy clinics', 'Allergy Clinics'), ('neurology', 'Neurology')], max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('present', 'Present'), ('leave', 'Leave')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(max_length=7)),
                ('token', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Others')], max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('phonenumber', models.IntegerField()),
                ('op', models.CharField(choices=[('general', 'General-1,2'), ('ent', 'ENT-8'), ('orthology', 'Orthology-3'), ('gynacology', 'Gynacology-5'), ('dental clinics', 'Dental Clinics-9'), ('psycology', 'Psycology-11'), ('pediatric clinics', 'Pediatric Clinics-6'), ('ophthalmology', 'Ophthalmology-7'), ('allergy clinics', 'Allergy Clinics-4'), ('neurology', 'Neurology-10')], max_length=100)),
                ('details', models.TextField(max_length=1000)),
                ('medicine', models.TextField(max_length=1000)),
                ('status', models.CharField(choices=[('emergency', 'Emergency'), ('waiting', 'Wating'), ('checked', 'Checked')], max_length=100)),
            ],
        ),
    ]
