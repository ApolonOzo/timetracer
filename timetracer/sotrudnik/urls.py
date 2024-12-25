from django.urls import path
from . import views
from .views import calendar_view, create_event


urlpatterns = [
    path('', views.sotrudnik),
    path('/calendar', calendar_view, name='calendar_view'),
    path('create', create_event, name='create_event')
]
