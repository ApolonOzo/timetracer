from django.shortcuts import render


def welcome(request):
    return render(request, 'main/welcome.html')

def register(request):
    return render(request, 'main/register.html')

def sotrudnik(request):
    return render(request, 'main/sotrudnik.html')