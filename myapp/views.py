from django.shortcuts import render,redirect
from myapp.models import *
from myapp.forms import *
from django.contrib.auth import login,logout

# Create your views here.


def register_patient(request):
    if request.method == 'POST':
        form_data=RegisterForm(request.POST)
        if form_data.is_valid():
            user_data= form_data.save(commit=False)
            user_data.user_type = "Patient"
            user_data.save()
            return redirect('login_page')
    form_data=RegisterForm()
    context={
        'form_data':form_data
    }
    return render(request, "register.html", context)


def register_doctor(request):
    if request.method == 'POST':
        form_data=RegisterForm(request.POST)
        if form_data.is_valid():
            user_data= form_data.save(commit=False)
            user_data.user_type = "Doctor"
            user_data.save()
            return redirect('login_page')
    form_data=RegisterForm()
    context={
        'form_data':form_data
    }
    return render(request, "register.html", context)


def login_page(request):
    if request.method == 'POST':
        form_data = loginForm(request, request.POST)
        if form_data.is_valid():
            user=form_data.get_user()
            login(request,user)
            return redirect('dashboard')

    form_data = loginForm()
    context = {"form_data": form_data}
    return render(request, "login.html", context)

def dashboard(request):
    return render(request,'dashboard.html')

def logout_page(request):
    logout(request)
    return redirect("login_page")
   
