from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse

from.models import *
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request,'about.html')

def page(request):
    return render(request,'page.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

def bookbtn(request):
    return render(request,'book.html')

def exist(request):
    return render(request,'home.html')

def loginbtn(request):
    return render(request,'login.html')

def adminbtn(request):
    return render(request,'admin.html')

def bloodbtn(request):
    return render(request,'blooddon.html')

def regpg(request):
    return render(request,'admindh.html')

def bills(request):
    return render(request,'bill.html')

def dash(request):
    return render(request, 'dashboard.html')


# create appoiment
def appointment_create(request):
    emplist={}
    try:
        datetime = request.POST['datetime']
        name = request.POST['name']
        gender = request.POST['gender']
        age = request.POST['age']
        place = request.POST['place']
        phonenumber = request.POST['phonenumber']
        bookingdate = request.POST['bookingdate']
        department = request.POST['op']
        status= request.POST['status']
        appointment=Appointment.objects.create(datetime=datetime,name=name,gender=gender,age=age,place=place,phonenumber=phonenumber,bookingdate=bookingdate,op=department,status=status)
        emplist['key']="appoiment is submited"
        return render(request,"book.html",emplist)
    except Exception as b:
        print(b)
        emplist['key']="apppoiment is not submit"
        return render(request,"book.html",emplist)

def delete(request):
    try:
        dlt=request.POST['dlt']
        Appointment.objects.filter(name=dlt).delete()
        return render(request,"dash1.html",{'del':'deleted'})
    except Exception as b:
        print(b)
        return render(request,"dash1.html",{'del':'not deleted '})
  
# contact enquery
def contact_enq(request):
    emplist={}
    try:
        name= request.POST['name']
        phonenumber= request.POST['phonenumber']
        contact= Enquery.objects.create(name=name, phonenumber=phonenumber)
        emplist['key1']="enquery  soon we will contact you"
        return render(request,"contact.html",emplist)
    except Exception as b:
        print(b)
        emplist['key1']="soory not submimted"
        return render(request,"contact.html",emplist)

# diplay department
def displayop(request):
    disp=Departments.objects.all()
    return render(request,"opdata.html",{'op': disp})

# blood donation form
def blooddonation_list(request):
    emplist1={}
    try:
        name= request.POST['names']
        place= request.POST['place']
        age= request.POST['age']
        gender= request.POST['gender']
        phonenumber= request.POST['phonenumber']
        bloodgroup= request.POST['bloodgroup']
        bloodlist=Blooddonation.objects.create(names=name, place=place,age=age,gender=gender,phonenumber=phonenumber,bloodgroup=bloodgroup)
        emplist1['key2']="your blood donation list is submited"
        return render(request,'blooddon.html', emplist1)
    except Exception as c:
        print(c)
        emplist1['key2']="soory not submiited"
        return render(request,'blooddon.html',emplist1)

# diplay  doctors data
def displaydoctors(request):
    disp=Doctors.objects.all()
    return render(request,"doctdis.html",{'dp': disp})

# display bloodbank data
def displaybloodbank(request):
    disp=Bloodbank.objects.all()
    return render(request,"bloodbank.html",{'db': disp})

# login form for sign up
def loginform(request):
    emplist = {}
    try:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user_exists = Doctors.objects.filter(username=username, password=password).exists()
            if user_exists:
                emplist['keys1'] = 'success login'
                return render(request, 'dashboard.html', emplist)
            else:
                emplist['keys1'] = 'invalid username or password'
                return render(request, 'login.html', emplist)
        else:
            return render(request, 'login.html')
    except Exception as b:
        print(b)
        emplist['keys1'] = 'error'
        return render(request, 'login.html', emplist)  

# ADMIN LOGIN FORM
def adminform(request):
    emplist = {}
    try:
        if request.method == 'POST':
            adminname = request.POST['adminname']
            passwords = request.POST['passwords']
            user_exists = Admins.objects.filter(adminname=adminname, passwords=passwords).exists()
            if user_exists:
                emplist['key5'] = 'success login'
                return render(request, 'admindh.html', emplist)
            else:
                emplist['key5'] = 'invalid username or password'
                return render(request, 'admin.html', emplist)
        else:
            return render(request, 'admin.html')
    except Exception as b:
        print(b)
        emplist['key5'] = 'error'
        return render(request, 'admin.html', emplist)    

# registration
def registerform(request):
    emplist2={}
    try:
        datetime=request.POST['datetime']
        token=request.POST['token']
        name=request.POST['name']
        age=request.POST['age']
        gender=request.POST['gender']
        place=request.POST['place']
        phonenumber=request.POST['phonenumber']
        op=request.POST['op']
        status=request.POST['status']
        reg=Registration.objects.create(datetime=datetime,token=token,name=name,age=age,gender=gender,place=place,phonenumber=phonenumber,op=op,status=status)
        emplist2['key6']="registration submit"
        return render(request,"admindh.html",emplist2)
    except Exception as b:
        print(b)
        emplist2['key6']="not submited"
        return render(request,'admindh.html',emplist2)


# billings
def billings(request):
    emp={}
    try:
        datetime=request.POST['datetime']
        name=request.POST['name']
        place=request.POST['place']
        phonenumber=request.POST['phonenumber']
        description=request.POST['description']
        payment=request.POST['payment']
        status=request.POST['status']
        amountdue=request.POST['amountdue']
        totalamount=request.POST['totalamount']
        bil=Bills.objects.create(datetime=datetime, name=name, place=place, phonenumber=phonenumber, description=description, payment=payment, status=status, amountdue=amountdue, totalamount=totalamount)
        emp['keyb']="submitted"
        return render(request,'bill.html',emp)
    except Exception as b:
        print(b)
        emp['keyb']='not submited'
        return render(request,'bill.html',emp)


# display op status
def displayopstatus(request):
    disp=Registration.objects.all()
    return render(request,"opstatus.html",{'dops': disp})


# display register status
def display_register(request):
    disp=Registration.objects.all()
    return render(request,"dashp.html",{'reg':disp})

def patients_status(request):    
    emp = {}
    try:
        if request.method == 'POST':
            status = request.POST['status']
            register = Registration.objects.update(status=status)
            register.save()
            emp['key6'] = "updated"
            return render(request, 'dashp.html', emp)
    except Exception as e:
        print(e)
        emp['key6'] = "error"
        return render(request, 'dashp.html',emp)


# appoiment status for doctors
def registrationdta(request,):
    disp=Appointment.objects.all()
    return render(request, "dash.html",{'aps': disp})

def user(request, id):
    a=Doctors.objects.get(id=id)
    return render(request,'dash.html',{'data':a})


def update1(request, id):
    xyz= get_object_or_404(Appointment,id=id)
    if request.method=='POST':
        status1= request.POST.get('status')
        xyz.status=status1
        xyz.save()

    return render(request,'dash.html',xyz)

def delete1(request,id):
    dele=Appointment.objects.get(id=id)
    dele.delete()
    return render(request,'dash.html')


# feed back
def feedback(request):
    emp={}
    try:
        name=request.POST['name']
        feedback=request.POST['feedback']
        feed=Feedback.objects.create(name= name, feedback=feedback)
        emp['feed']='submit your feed back'
        return render(request,'blog.html',emp)
    except Exception as b:
        print(b)
        emp['feed']= "soory"
        return render(request,'blog.html',emp)

