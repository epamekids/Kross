from django.shortcuts import render

def page(request):
    return render(request, 'Home1/homePage.html')
