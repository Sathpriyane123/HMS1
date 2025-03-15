from django.urls import path
from.import views

urlpatterns=[
    path('',views.home, name='home'),

    path('bookbtn',views.bookbtn,name='bookbtn'),
    path('appointment',views.appointment_create,name="appointment"),
    path('home1', views.exist,name='home1'),
    path('loginbtn',views.loginbtn,name='loginbtn'),

    path('Loginform',views. loginform,name='Loginform'),
    path('dashbord',views.dash, name='dashbord'),
    path('appointmentstatus',views.registrationdta, name='appointmentstatus'),
    path('appointmentstatus/<int:id>',views.user, name='appointmentstatus'),

    path('patient',views.display_register,name='patient'),
    path('patient/<int:id>',views.patients_status,name='patient'),

    path('edit1/<int:id>', views.update1, name='edit1'),
    path('delete1/<int:id>', views.delete1, name='delete1'),

    
    path('adminbtn',views.adminbtn,name='adminbtn'),
    path('adminform',views.adminform,name='adminform'),
    path('registerform',views.registerform, name='registerform'),
    path('register',views.regpg,name='register'),
    path('bills',views.bills, name='bills'),
    path('billing',views.billings, name='billing'),
    path('feedbacks', views.feedback,name='feedbacks'),

    path('about',views.about,name='about'),

    path('page',views.page,name='page'),
    path('displayop',views.displayop,name='displayop'),
    path('bloodbtn',views.bloodbtn, name='bloodbtn'),
    path('blooddonation',views.blooddonation_list,name='bloodonation'),
    path('displaydoctors',views.displaydoctors,name='displaydoctors'),
    path('bloodbank',views.displaybloodbank,name='bloodbank'),
    path('opstatus',views.displayopstatus, name='opstatus'),

    path('blog',views.blog,name='blog'),
    path('contact',views.contact,name='contact'),
    path('enqury',views.contact_enq,name='enqury'),

]