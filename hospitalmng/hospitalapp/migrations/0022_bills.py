# Generated by Django 5.0 on 2024-01-22 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0021_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(max_length=7)),
                ('name', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('phonenumber', models.IntegerField()),
                ('description', models.TextField(max_length=1000)),
                ('payment', models.CharField(choices=[('cash payment', 'Cash payment'), ('upi', 'UPI'), ('credit/debit', 'Credit/Debit')], max_length=100)),
                ('status', models.CharField(choices=[('pendding', 'Pending'), ('completed', 'Completed')], max_length=100)),
                ('amountdue', models.IntegerField()),
                ('totalamount', models.IntegerField()),
            ],
        ),
    ]
