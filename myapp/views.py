from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import EmployeeData
import re
# Create your views here.

@login_required(login_url='login')
def Employeedata(request):
    data = EmployeeData.objects.all()
    return render(request, 'employeedata.html',{'data':data})

@login_required(login_url='login')
def home(request):
    if request.method == 'POST':
        name_n = request.POST.get('name')
        email_n = request.POST.get('email')
        phone_n = request.POST.get('phone')
        gender_n = request.POST.get('gender')
        address_n = request.POST.get('address')
        education_n = request.POST.get('education')
        experince_n = request.POST.get('experince')
        pincode_n = request.POST.get('pincode')
        pattern = r'^\d{10}$'
        zipcode = r'^\d{6}$'
        
        if name_n is None or name_n == '':
            messages.error(request,'Please enter name !')
            return redirect('home')
        elif email_n is None or email_n == '':
            messages.error(request,'Please enter  email id !')
            return redirect('home')
        elif not re.match(pattern,phone_n ):
            messages.error(request,'Please enter a valid 10-digit mobile number ! ')
            return redirect('home')
        elif gender_n is None or gender_n == '':
            messages.error(request,'Please enter Gender')
            return redirect('home')
        elif address_n is None or address_n == '':
            messages.error(request,'Please enter Address !')
            return redirect('home')
        elif education_n is None or education_n == '':
            messages.error(request,'Please enter E=Qualificatons !')
            return redirect('home')
        elif experince_n is None or experince_n == '':
            messages.error(request,'Please enter Work Experince !.')
            return redirect('home')
        elif not re.match(zipcode,pincode_n ):
            messages.error(request,'Please enter a valid 6-digit PIN code!')
            return redirect('home')
        else:
            data = EmployeeData(name=name_n, email=email_n, phone= phone_n, gender=gender_n,address=address_n, education=education_n, experince=experince_n,pincode=pincode_n)
            data.save()
            messages.success(request, 'Your form submit !')
            return redirect('home')
            
    return render(request, 'index.html')




@login_required(login_url='login')
def updatedata(request, pk):
    employee = get_object_or_404(EmployeeData, pk=pk)
    if request.method == 'POST':
        employee.name = request.POST.get('name')
        employee.email = request.POST.get('email')
        employee.phone = request.POST.get('phone')
        employee.gender = request.POST.get('gender')
        employee.address = request.POST.get('address')
        employee.education = request.POST.get('education')
        employee.experince = request.POST.get('experince')
        employee.pincode = request.POST.get('pincode')

        
        if employee.name is None or employee.name == '':
            messages.error(request, 'Please enter name!')
            return redirect('employeeupdate', pk=pk)
        if employee.email is None or employee.email == '':
            messages.error(request, 'Please enter email id!')
            return redirect('employeeupdate', pk=pk)
        if employee.phone is None or employee.phone == '':
            messages.error(request,'Please enter a valid 10-digit mobile number ! ')
            return redirect('employeeupdate', pk=pk)
        if employee.gender is None or employee.gender == '':
            messages.error(request, 'Please enter Gender!')
            return redirect('employeeupdate', pk=pk)
        if employee.address is None or employee.address == '':
            messages.error(request, 'Please enter Address!')
            return redirect('employeeupdate', pk=pk)
        if employee.education is None or employee.education == '':
            messages.error(request, 'Please enter Qualifications!')
            return redirect('employeeupdate', pk=pk)
        if employee.experince is None or employee.experince == '':
            messages.error(request, 'Please enter Work Experience!')
            return redirect('employeeupdate', pk=pk)
        if employee.pincode is None or employee.pincode == '':
            messages.error(request,'Please enter a valid 6-digit PIN code!')
            return redirect('employeeupdate', pk=pk)
        else:
            employee.save()
            messages.success(request, 'Update your form!')
            return redirect('employeedata')

    return render(request, 'updatedat.html', {'employee': employee})

@login_required(login_url='login')
def Deletedata(request, pk):
    data = EmployeeData.objects.get(pk=pk)
    data.delete()
    return redirect('employeedata')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
            
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login') 




def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not username or not password or not confirm_password:
            messages.error(request, 'Please fill in all the fields.')
            return redirect('register')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
            return redirect('register')

        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, 'user Created successfully !')
        return redirect('login')

    return render(request, 'register.html')

