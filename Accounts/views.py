from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from Accounts.forms import SignUp, LogIn
from django.http import HttpResponse


class SignUp(FormView):
    form_class = UserCreationForm
    success_url = "/"
    template_name = "registration/isingUp.html"

    def form_valid(self, form):
      form.save()
      return super(SignUp, self).form_valid(form)

def login(request):
    if request.method == 'POST':
        form = LogIn(request.POST)
        if form.is_valid():
            if form.get_user():
                login(request, form.get_user())
                return HttpResponseRedirect('/')
    else:
        form = LogIn()
    return render(request, 'registration/signIn.html', {'form': form})



def signup(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('/')
    else:
        form = SignUp()
    return render(request, 'registration/signUp.html', {'form': form})
