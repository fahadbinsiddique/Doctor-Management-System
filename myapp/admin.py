from django.contrib import admin
from myapp.models import*

# Register your models here.

admin.site.register([UserInfoModel,DepartmentModel,DoctorModel,PatientModel,ProfileModel])
