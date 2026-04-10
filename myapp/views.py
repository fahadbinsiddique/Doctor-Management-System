from django.shortcuts import render, redirect
from myapp.models import *
from myapp.forms import *
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def register_patient(request):
    if request.method == "POST":
        form_data = RegisterForm(request.POST)
        if form_data.is_valid():
            user_data = form_data.save(commit=False)
            user_data.user_type = "Patient"
            user_data.save()
            return redirect("login_page")
    form_data = RegisterForm()
    context = {
        "form_data": form_data,
        "title": "Add Patient Register",
        "btn": "Add Patient",
    }
    return render(request, "register.html", context)


def register_doctor(request):
    if request.method == "POST":
        form_data = RegisterForm(request.POST)
        if form_data.is_valid():
            user_data = form_data.save(commit=False)
            user_data.user_type = "Doctor"
            user_data.save()
            return redirect("login_page")
    form_data = RegisterForm()
    context = {
        "form_data": form_data,
        "title": "Add Doctor Register",
        "btn": "Add Doctor",
    }
    return render(request, "register.html", context)


def login_page(request):
    if request.method == "POST":
        form_data = loginForm(request, request.POST)
        if form_data.is_valid():
            user = form_data.get_user()
            login(request, user)
            return redirect("dashboard")

    form_data = loginForm()
    context = {"form_data": form_data}
    return render(request, "login.html", context)


@login_required
def dashboard(request):

    return render(request, "dashboard.html")


def home(request):

    return render(request, "home.html")


@login_required
def logout_page(request):
    logout(request)
    return redirect("login_page")


@login_required
def add_department(request):
    if request.method == "POST":
        form_data = Add_Department_Form(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect("department_list")
    form_data = Add_Department_Form()
    context = {
        "form_data": form_data,
        "title": "Add Department Info",
        "heading": "Add Department Info",
        "btn": "Add Department",
    }
    return render(request, "master/base-form.html", context)


@login_required
def department_list(request):
    form_data = DepartmentModel.objects.all()
    context = {
        "form_data": form_data,
        "heading": "All Department List",
        "title": "Department List",
    }
    return render(request, "department/department_list.html", context)


@login_required
def edit_department(request, d_id):
    selected_department = DepartmentModel.objects.get(id=d_id)
    if request.method == "POST":
        form_data = Add_Department_Form(request.POST, instance=selected_department)
        if form_data.is_valid():
            form_data.save()
            return redirect("department_list")
    form_data = Add_Department_Form(instance=selected_department)
    context = {
        "form_data": form_data,
        "title": "Edit Department Info",
        "heading": "Edit Department Info",
        "btn": "Update Department",
    }
    return render(request, "master/base-form.html", context)


@login_required
def view_department(request, d_id):
    form_data = DepartmentModel.objects.get(id=d_id)
    all_doctor = DoctorModel.objects.all()
    context = {"form_data": form_data, "title": "view", "all_doctor": all_doctor}
    return render(request, "department/view_department.html", context)


@login_required
def delete_department(request, d_id):
    DepartmentModel.objects.get(id=d_id).delete()
    return redirect("department_list")


@login_required
def add_doctor(request):
    if request.method == "POST":
        form_data = Add_Doctor_Form(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect("doctor_list")
    form_data = Add_Doctor_Form()
    context = {
        "form_data": form_data,
        "title": "Add Doctor Info",
        "heading": "Add Doctor Info",
        "btn": "Add Doctor",
    }
    return render(request, "master/base-form.html", context)


@login_required
def doctor_list(request):
    form_data = DoctorModel.objects.all()
    context = {
        "form_data": form_data,
        "heading": "All Doctor Info",
        "title": "Doctor List",
    }
    return render(request, "doctor/doctor_list.html", context)


@login_required
def edit_doctor(request, d_id):
    selected_department = DoctorModel.objects.get(id=d_id)
    if request.method == "POST":
        form_data = Add_Doctor_Form(request.POST, instance=selected_department)
        if form_data.is_valid():
            form_data.save()
            return redirect("doctor_list")
    form_data = Add_Doctor_Form(instance=selected_department)
    context = {
        "form_data": form_data,
        "title": "Edit Doctor Info",
        "heading": "Edit Doctor Info",
        "btn": "Update Doctor",
    }
    return render(request, "master/base-form.html", context)


@login_required
def view_doctor(request, d_id):
    form_data = DoctorModel.objects.get(id=d_id)
    patient_data = PatientModel.objects.all()
    context = {"form_data": form_data, "title": "view", "patient_data": patient_data}
    return render(request, "doctor/view_doctor.html", context)


@login_required
def delete_doctor(request, d_id):
    DoctorModel.objects.get(id=d_id).delete()
    return redirect("doctor_list")


@login_required
def add_patient(request):
    if request.method == "POST":
        form_data = Add_Patient_Form(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect("patient_list")
    form_data = Add_Patient_Form()
    context = {
        "form_data": form_data,
        "title": "Add Patient Info",
        "heading": "Add Patient Info",
        "btn": "Add Patient",
    }
    return render(request, "master/base-form.html", context)


@login_required
def patient_list(request):
    form_data = PatientModel.objects.all()
    context = {
        "form_data": form_data,
        "heading": "All Paitent Info",
        "title": "Paitent List",
    }
    return render(request, "patient/patient_list.html", context)


@login_required
def edit_patient(request, d_id):
    selected_department = PatientModel.objects.get(id=d_id)
    if request.method == "POST":
        form_data = Add_Patient_Form(request.POST, instance=selected_department)
        if form_data.is_valid():
            form_data.save()
            return redirect("patient_list")
    form_data = Add_Patient_Form(instance=selected_department)
    context = {
        "form_data": form_data,
        "title": "Edit Paitent Info",
        "heading": "Edit Paitent Info",
        "btn": "Update Paitent",
    }
    return render(request, "master/base-form.html", context)


@login_required
def view_patient(request, d_id):
    form_data = PatientModel.objects.get(id=d_id)
    context = {"form_data": form_data, "title": "view"}
    return render(request, "patient/view_patient.html", context)


@login_required
def delete_patient(request, d_id):
    PatientModel.objects.get(id=d_id).delete()
    return redirect("patient_list")
