from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class SignUp(forms.Form):
    nickname = forms.CharField(label = "Your nickname",required=True)
    password = forms.CharField(label = "Your password",required=True)
    password_confirm = forms.CharField(label = "Confirm your password",required=True)
    email = forms.EmailField(label ="Your email address",required=True)

class LogIn(forms.Form):
    nickname = forms.CharField(label = "Your nickname",required=True)
    password = forms.CharField(label = "Your password", required=True)
