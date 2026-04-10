from django import forms
from myapp.models import * 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model=UserInfoModel
        fields = ["username", "full_name", "address",]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})


class loginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})
