# weather_app/urls.py
from django.urls import path
from .views import weather_home

urlpatterns = [
    path('', weather_home, name='weather_home'),
]
