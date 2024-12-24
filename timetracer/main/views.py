from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')

def welcome(request):
    return render(request, 'main/welcome.html')

def register(request):
    return render(request, 'main/register.html')

def password(request):
    return render(request, 'main/password.html')





