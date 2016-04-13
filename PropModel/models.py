
from django.db import models

from datetime import date, datetime, timedelta

# Create your models here.

class Gender(models.Model):
    gender = models.CharField(max_length=1)
    def __str__(self):
        return self.gender
        
class Student(models.Model):
    ID = models.IntegerField(blank=True,null=True)
    First_Name = models.CharField(max_length=50,blank=True,null=True)
    Last_Name = models.CharField(max_length=50,blank=True,null=True)
    gender = models.ForeignKey(Gender)
    Birth_Date = models.DateField('Birth Date',blank=True,null=True)
    School = models.CharField(max_length=50,blank=True,null=True)
    Class = models.IntegerField(blank=True,null=True)
    Address = models.CharField(max_length=200,blank=True,null=True)
    Father_Name = models.CharField(max_length=50,blank=True,null=True)
    Mother_Name = models.CharField(max_length=50,blank=True,null=True)
    Teacher_Name = models.CharField(max_length=50,blank=True,null=True)
    def __str__(self):
        return self.First_Name
    
class Payment(models.Model):
    ID = models.IntegerField(blank=True,null=True)
    Bank_Name = models.CharField(max_length=50,blank=True,null=True)
    Bank_Account_Number = models.IntegerField(blank=True,null=True)
    Payment_Date = models.DateField('Date Paid',blank=True,null=True)
    Payment_Amount = models.IntegerField(blank=True,null=True)
    Pay_By = models.CharField(max_length=50,blank=True,null=True)
    Receipt_Confirmation_Date = models.DateField('Receipt Confirmed',blank=True,null=True)
    def __str__(self):
        return self.Bank_Name
    

    

