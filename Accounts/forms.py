from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUp(UserCreationForm):
    nickname = forms.CharField(label = "Your Nickname",required=True)
    firstname = forms.CharField(label ="First Name",required=False)
    lastname = forms.CharField(label ="Last Name",required=False)
    email = forms.EmailField(label ="Your Email Address",required=True)

class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
