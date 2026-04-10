from myapp.views import *
from django.urls import path

urlpatterns = [
    path("register-patient/", register_patient, name="register_patient"),
    path("register-doctor/", register_doctor, name="register_doctor"),
    path("login/", login_page, name="login_page"),
    path("dashboard/", dashboard, name="dashboard"),
    path("logout/", logout_page, name="logout_page"),
    # path("register",)
]
