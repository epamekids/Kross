from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUp(forms.Form):
    nickname = forms.CharField(label = "Your nickname",required=True)
    password = forms.CharField(label = "Your password",required=True)
    password_confirm = forms.CharField(label = "Confirm your password",required=True)
    firstname = forms.CharField(label ="First name",required=False)
    lastname = forms.CharField(label ="Last name",required=False)
    email = forms.EmailField(label ="Your email address",required=True)

class LogIn(forms.Form):
    nickname = forms.CharField(label = "Your nickname",required=True)
    password = forms.CharField(label = "Your password", required=True)
