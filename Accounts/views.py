from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from Accounts.forms import SignUp, LogIn
from django.http import HttpResponse
from Accounts.models import User

def login(request):
    try:
        return render(request, 'registration/signIn.html', {'form': LogIn()})
        member = User.objects.get(nickname=request.POST.get('nickname'))
        if member.password == request.POST['password']:
            request.session['member_id'] = member.id
            return HttpResponse("You have successfully signed in.")
            return redirect('/')
    except User.DoesNotExist:
        return HttpResponse("Sorry, but something went wrong.")


def signup(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
            User.nickname = nickname
            User.password = password
            User.email = email
    else:
        form = SignUp()
    return render(request, 'registration/signUp.html', {'form': SignUp()})
