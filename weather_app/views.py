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
    current_weather = response.json()

    forecast_url = "http://api.openweathermap.org/data/2.5/forecast"
    forecast_params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',
    }
    forecast_response = requests.get(forecast_url, params=forecast_params)
    forecast_data = forecast_response.json()

    return current_weather, forecast_data['list']

def weather_home(request):
    api_key = 'de1f124bf2344600239ce77ed33c4f75'
    city = request.GET.get('city', 'Dhaka')  # Default city is Dhaka

    current_weather, forecast_data = get_weather(api_key, city)

    context = {
        'city': city,
        'current_weather': current_weather,
        'forecast_data': forecast_data,
    }

    return render(request, 'weather_home.html', context)
