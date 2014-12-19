from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.Form):
    username   = forms.CharField(label="Username", max_length=30)
    first_name = forms.CharField(label="First Name", max_length=30)
    last_name  = forms.CharField(label="Last Name", max_length=30)
    register_swear = forms.BooleanField(
        label="I solemnly swear that I am up to no bad!",
        required=False
    )

    def clean_register_swear(self):
        swore = self.cleaned_data.get('register_swear')
        if not swore:
            raise forms.ValidationError("You need to give your word. Don't [Br]eak [Ba]d! I am Sirius!")
            return False
        return True


class LoginForm(forms.Form):
    username  = forms.CharField(label="Username", max_length=30)
    password  = forms.CharField(label="Password", max_length=30)
    login_rem = forms.BooleanField(label="Remember me")


class PasswordChangeForm(forms.Form):
    password_old = forms.CharField(label="Original Password", max_length=30)
    password     = forms.CharField(label="New Password", max_length=30)
    password_re  = forms.CharField(label="Confirm Password", max_length=30)

    def clean_password_re(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password_re')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError("The passwords didn't match.")
        return password2


class PasswordResetRequestForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30)


class PasswordResetChangeForm(forms.Form):
    password    = forms.CharField(label="Password", max_length=30)
    password_re = forms.CharField(label="Confirm Password", max_length=30)

    def clean_password_re(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password_re')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError("The passwords didn't match.")
        return password2
