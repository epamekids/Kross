from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUp(forms.Form):
    nickname = forms.CharField(label = "Your nickname",required=True)
    password = forms.CharField(label = "Your password",required=True)
    password_confirm = forms.CharField(label = "Confirm your password",required=True)
    email = forms.EmailField(label ="Your email address",required=True)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username == None:
           return self.cleaned_data

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 == password2:
            return self.cleaned_data


class LogIn(forms.Form):
    nickname = forms.CharField(label = "Your nickname",required=True)
    password = forms.CharField(label = "Your password", required=True)

    def clean(self):
        cleaned_data = super(LogIn, self).clean()
        if not self.errors:
            user = authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
            if user is None:
                raise forms.ValidationError("Nickname or password are wrong.")
            self.user = user
        return cleaned_data

    def get_user(self):
        return self.user or None
