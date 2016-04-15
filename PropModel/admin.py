from django.contrib import admin

# Register your models here.
from .models import Gender
from .models import Student
from .models import Payment
from .models import Volunteer

class StudentAdmin(admin.ModelAdmin):
    list_display = ('First_Name', 'Last_Name')
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('Bank_Name','Bank_Account_Number')
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('Phone_Number','Email','Company')
admin.site.register(Gender)
admin.site.register(Student,StudentAdmin)
admin.site.register(Payment,PaymentAdmin)
admin.site.register(Volunteer,VolunteerAdmin)


