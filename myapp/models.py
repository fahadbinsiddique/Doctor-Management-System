from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserInfoModel(AbstractUser):
    USER_TYPE = [
        ("Admin", "Admin"),
        ("Doctor", "Doctor"),
        ("Patient", "Patient"),
    ]
    full_name = models.CharField(max_length=100, null=True)
    address = models.TextField(null=True)
    user_type = models.CharField(choices=USER_TYPE, max_length=20, null=True)

    def __str__(self):
        return f'{self.username}'

class ProfileModel(models.Model):
    user=models.OneToOneField(
        UserInfoModel,
        on_delete=models.CASCADE,
        related_name='user_profile',
        null=True,
    )
    profile_pic=models.ImageField(upload_to='media/',null=True)
    phone_number=models.CharField(max_length=20, null=True)

    def __str__(self):
        return f'{self.user}'


class DepartmentModel(models.Model):

    name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class DoctorModel(models.Model):

    name = models.CharField(max_length=120, null=True)
    email = models.EmailField(max_length=120, null=True)
    phone = models.CharField(max_length=100, null=True)
    specialization = models.CharField(max_length=100, null=True)
    department = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE)
    joining_date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class PatientModel(models.Model):
    name = models.CharField(max_length=120, null=True)
    age = models.IntegerField(null=True)
    gender = models.der = models.CharField(max_length=120, null=True)
    disease = models.TextField(null=True)
    doctor = models.ForeignKey(DoctorModel, on_delete=models.CASCADE)
    admit_date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
