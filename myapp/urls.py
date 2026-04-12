from myapp.views import *
from django.urls import path

urlpatterns = [
    path("", home, name="home"),
    path("register-admin/", register_admin, name="register_admin"),
    path("register-patient/", register_patient, name="register_patient"),
    path("register-doctor/", register_doctor, name="register_doctor"),
    path("login/", login_page, name="login_page"),
    path("dashboard/", dashboard, name="dashboard"),
    path("profile/", profile, name="profile"),
    path("logout/", logout_page, name="logout_page"),
    path("add-department/", add_department, name="add_department"),
    path("department-list/", department_list, name="department_list"),
    path("department-edit/<str:d_id>/", edit_department, name="edit_department"),
    path("department-view/<str:d_id>/", view_department, name="view_department"),
    path("department-delete/<str:d_id>/", delete_department, name="delete_department"),
    path("add-doctor/", add_doctor, name="add_doctor"),
    path("doctor-list/", doctor_list, name="doctor_list"),
    path("doctor-edit/<str:d_id>/", edit_doctor, name="edit_doctor"),
    path("doctor-view/<str:d_id>/", view_doctor, name="view_doctor"),
    path("doctor-delete/<str:d_id>/", delete_doctor, name="delete_doctor"),
    path("add-patient/", add_patient, name="add_patient"),
    path("patient-list/", patient_list, name="patient_list"),
    path("patient-edit/<str:d_id>/", edit_patient, name="edit_patient"),
    path("patient-view/<str:d_id>/", view_patient, name="view_patient"),
    path("patient-delete/<str:d_id>/", delete_patient, name="delete_patient"),
]
