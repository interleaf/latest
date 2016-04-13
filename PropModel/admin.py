from django.contrib import admin

# Register your models here.
from .models import Gender
from .models import Student
from .models import Payment

class StudentAdmin(admin.ModelAdmin):
    list_display = ('First_Name', 'Last_Name')
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('Bank_Name','Bank_Account_Number')
        
admin.site.register(Gender)
admin.site.register(Student,StudentAdmin)
admin.site.register(Payment,PaymentAdmin)



