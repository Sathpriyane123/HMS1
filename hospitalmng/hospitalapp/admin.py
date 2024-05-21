from django.contrib import admin
from.models import *

# Register your models here.


class AppoinmentAdmin(admin.ModelAdmin):
     list_display=('datetime','name','gender','age','place','phonenumber','bookingdate','op','status')
admin.site.register(Appointment,AppoinmentAdmin)

class EnqueryAdmin(admin.ModelAdmin):
     list_display=('name', 'phonenumber')
admin.site.register(Enquery,EnqueryAdmin)

class DepartmentsAdmin(admin.ModelAdmin):
     list_display=('op', 'department','floor')
admin.site.register(Departments,DepartmentsAdmin)

class BlooddonationAdmin(admin.ModelAdmin):
     list_display=('names', 'place', 'age', 'gender', 'bloodgroup')
admin.site.register(Blooddonation,BlooddonationAdmin)


class DoctorsAdmin(admin.ModelAdmin):
     list_display=('doctorsname', 'op', 'username', 'password', 'status')
admin.site.register(Doctors,DoctorsAdmin)

class BloodbankAdmin(admin.ModelAdmin):
     list_display=('bloodgroup', 'unit')
admin.site.register(Bloodbank,BloodbankAdmin)

class RegistertionAdmin(admin.ModelAdmin):
     list_display=('datetime', 'token', 'name', 'age', 'gender', 'place', 'phonenumber', 'op', 'status')
admin.site.register(Registration,RegistertionAdmin)


class AdminsAdmin(admin.ModelAdmin):
     list_display=('adminname', 'passwords')
admin.site.register(Admins,AdminsAdmin)

class FeedAdmin(admin.ModelAdmin):
     list_display=('name','feedback')
admin.site.register(Feedback,FeedAdmin)

class BillsAdmin(admin.ModelAdmin):
     list_display=('datetime', 'name', 'place', 'phonenumber', 'description', 'payment', 'status', 'amountdue', 'totalamount')
admin.site.register(Bills,BillsAdmin)