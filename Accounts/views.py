from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from Accounts.forms import UserCreateForm

def profile(request):
    return render(request, "registration/profile.html")

def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)

        if  form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username,password=password)
            login(request, user)
            return redirect("/accounts/profile")
    else:
        form = UserCreateForm()

    context = {"form":form}
    return render(request, 'registration/register.html', context)
