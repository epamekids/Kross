from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from Accounts.forms import SignUp, LogIn
from django.http import HttpResponse
from Accounts.models import User

def login(request):
  try:
      member = request.session.get(username=request.POST['username'])
      if member.password == request.POST['password']:
          request.session['member_id'] = member.id
          return HttpResponse("You're signed in.")
  except User.DoesNotExist:
      return HttpResponse("Your nickname or password is incorrect. Try again.")

def signup(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/register')
    else:
        form = SignUp()
    return render(request, 'registration/signUp.html', {'form': SignUp()})
