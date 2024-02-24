# Django Weather App with 5-Day Forecast

## Overview

This Django Weather App is a web application that provides users with current weather information and a 5-day forecast based on a specified city. The application integrates with the OpenWeatherMap API to fetch weather data.

## Features

- **Current Weather:** Displays the current temperature, weather description, humidity, and wind speed for the specified city.

- **5-Day Forecast:** Presents a 5-day weather forecast, including temperature, weather description, humidity, and wind speed.

## Prerequisites

Before running the application, make sure you have the following installed:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [OpenWeatherMap API Key](https://openweathermap.org/api)

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/md-fahim-bhuiyan/weather_app_project.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-weather-app
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up API Key:

   - Sign up on the [OpenWeatherMap website](https://openweathermap.org/api) to obtain a free API key.

   - Update the API key in the `settings.py` file.

5. Run migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Start the development server:

    ```bash
    python manage.py runserver
    ```

7. Access the application in your web browser at [http://localhost:8000/](http://localhost:8000/)

## Usage

- Visit the home page.
- Enter the city for which you want to check the weather and click "Get Weather."
- View the current weather information and the 5-day forecast.




