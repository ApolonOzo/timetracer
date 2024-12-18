from django.urls import path
from . import views
from .views import welcome

urlpatterns = [
    path('', views.welcome),
    path('register', views.register),
    path('sotrudnik', views.sotrudnik)
]
