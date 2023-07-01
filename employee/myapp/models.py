from django.db import models

# Create your models here.



class EmployeeData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField(max_length=15)
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    experince = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    