from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.Form):

    username   = forms.CharField(label="Username", max_length=30)
    first_name = forms.CharField(label="First Name", max_length=30)
    last_name  = forms.CharField(label="Last Name", max_length=30)


class LoginForm(forms.Form):

    username   = forms.CharField(label="Username", max_length=30)
    password   = forms.CharField(label="Password", max_length=30)
    login_rem  = forms.BooleanField(label="Remember me")


class PasswordResetRequestForm(forms.Form):

    username   = forms.CharField(label="Username", max_length=30)
