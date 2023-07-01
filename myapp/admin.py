from django.contrib import admin
from .models import EmployeeData
# Register your models here.

class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','gender','address','education','experince','pincode')

admin.site.register(EmployeeData, EmployeeModelAdmin)