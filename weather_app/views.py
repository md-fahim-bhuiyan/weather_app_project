# weather_app/views.py
from django.shortcuts import render
import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',
    }
    response = requests.get(base_url, params=params)
    weather_data = response.json()
    return weather_data

def weather_home(request):
    api_key = 'de1f124bf2344600239ce77ed33c4f75'
    city = request.GET.get('city', 'Dhaka')  

    weather_data = get_weather(api_key, city)

    context = {
        'city': city,
        'weather_data': weather_data,
    }

    return render(request, 'weather_home.html',context)
