from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home),
    path('welcome', views.welcome),
    path('register', views.register),
    path('password', views.password),
    path('welcome', include('sotrudnik.urls'))
]
