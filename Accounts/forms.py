from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model=User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self,  *args,  **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'mdl-textfield__input'
        self.fields['email'].widget.attrs['class'] = 'mdl-textfield__input'
        self.fields['password1'].widget.attrs['class'] = 'mdl-textfield__input'
        self.fields['password2'].widget.attrs['class'] = 'mdl-textfield__input'

    def save(self, commit=True):
      user = super(UserCreateForm, self).save(commit=False)
      user.email = self.cleaned_data["email"]
      if commit:
          user.save()
      return user
