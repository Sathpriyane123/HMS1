from django.db import models

# Create your models here.

class Appointment(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Others'),
    ]
    DEPARTMENT_CHOICES = [
        ('general', 'General'),
        ('ent', 'ENT'),
        ('orthology', 'Orthology'),
        ('gynacology', 'Gynacology'),
        ('dental clinics','Dental Clinics'),
        ('psycology','Psycology'),
        ('pediatric clinics', 'Pediatric Clinics'),
        ('ophthalmology','Ophthalmology'),
        ('allergy clinics','Allergy Clinics'),
        ('neurology','Neurology'),
    ]
    statuss_choice=[
        ('booked','Booked'),
        ('postponed','Postponed'),
        ('confirmed','Confirmed'),
        ('checked','Checked'),
        ('cancelled','Cancelled'),
    ]
    datetime = models.DateTimeField(max_length=10)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    age = models.IntegerField()
    place = models.CharField(max_length=100)
    phonenumber = models.IntegerField()
    bookingdate = models.DateField(max_length=10)
    op = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)
    status=models.CharField(max_length=100,choices=statuss_choice)
    def __str__(self):
        return self.name
    

# enquery table
class Enquery(models.Model):
    name= models.CharField(max_length=100)
    phonenumber=models.IntegerField()
    def __str__(self):
        return self.name
    
# # department and op
class Departments(models.Model):
    op=models.IntegerField()
    department=models.CharField(max_length=100)
    floor=models.CharField(max_length=10)
    def __str__(self):
        return self.department
    

    #blood donation  
class Blooddonation(models.Model):
    gender_choice=[
        ('male','Male'),
        ('female', 'Female'),
        ('other','Other'),
    ]

    blood_group=[
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    ]
    names=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=10 , choices=gender_choice)
    phonenumber=models.IntegerField()
    bloodgroup=models.CharField(max_length=10, choices=blood_group)
    def __str__(self):
        return self.names


# doctors data
class Doctors(models.Model):
    department_choices=[
        ('general', 'General'),
        ('ent', 'ENT'),
        ('orthology', 'Orthology'),
        ('gynacology', 'Gynacology'),
        ('dental clinics','Dental Clinics'),
        ('psycology','Psycology'),
        ('pediatric clinics', 'Pediatric Clinics'),
        ('ophthalmology','Ophthalmology'),
        ('allergy clinics','Allergy Clinics'),
        ('neurology','Neurology'),
    ]
    status_choicess=[
        ('present','Present'),
        ('leave','Leave'),
    ]
    doctorsname=models.CharField(max_length=200)
    op=models.CharField(max_length=100, choices=department_choices)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    status=models.CharField(max_length=50, choices=status_choicess)
    def __str__(self):
        return self.doctorsname
    
# blood bank datas
class Bloodbank(models.Model):
    bloodgroup_choice=[
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    ]
    bloodgroup=models.CharField(max_length=10, choices=bloodgroup_choice)
    unit=models.IntegerField()
    def __str__(self):
        return self.bloodgroup

# registration datas
class Registration(models.Model):
    GENDER_CHOICESS = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Others'),
    ]
    op_choices=[
        ('general', 'General-1,2'),
        ('ent', 'ENT-8'),
        ('orthology', 'Orthology-3'),
        ('gynacology', 'Gynacology-5'),
        ('dental clinics','Dental Clinics-9'),
        ('psycology','Psycology-11'),
        ('pediatric clinics', 'Pediatric Clinics-6'),
        ('ophthalmology','Ophthalmology-7'),
        ('allergy clinics','Allergy Clinics-4'),
        ('neurology','Neurology-10'),
    ]
    status_choice=[
        ('emergency', 'Emergency'),
        ('waiting', 'Waiting'),
        ('checking','Checking'),
        ('checked','Checked'),
    ]
    datetime=models.DateTimeField(max_length=7)
    token=models.IntegerField()
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=100, choices=GENDER_CHOICESS)
    place=models.CharField(max_length=100)
    phonenumber=models.IntegerField()
    op=models.CharField(max_length=100, choices=op_choices)
    status=models.CharField(max_length=100, choices=status_choice)
    def __str__(self):
        return self.name  

# billlingdata
class Bills(models.Model):
    payment_choice=[
        ('cash payment', 'Cash payment'),
        ('upi', 'UPI'),
        ('credit/debit','Credit/Debit'),
    ]
    status_choice=[
        ('pendding','Pending'),
        ('completed', 'Completed'),
    ]
    datetime=models.DateTimeField(max_length=7)
    name=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    phonenumber=models.IntegerField()
    description=models.TextField(max_length=1000)
    payment=models.CharField(max_length=100, choices=payment_choice)
    status=models.CharField(max_length=100, choices=status_choice)
    amountdue=models.IntegerField()
    totalamount=models.IntegerField()
    def __str__(self):
        return self.name


#  admin password
class Admins(models.Model):
    adminname=models.CharField(max_length=100)
    passwords=models.CharField(max_length=100)
    def __str__(self):
        return self.adminname

# feedback table
class Feedback(models.Model):
    name=models.CharField(max_length=100)
    feedback=models.CharField(max_length=500)
    def __str__(self):
        return self.name