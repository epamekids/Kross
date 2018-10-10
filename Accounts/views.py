from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from Accounts.forms import SignUp


def login(request):
    return render(request, 'registration/login.html', {'form': SignUp()})

def signup(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUp()
    return render(request, 'registration/signUp.html', {'form': form})
