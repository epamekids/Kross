from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from Accounts.forms import SignUp, LogIn
from django.http import HttpResponse
from Accounts.models import User

def signup(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SignUp()
    return render(request, 'registration/signUp.html', {'form': SignUp()})
