import requests

import API

weather_api = API.weather_api
api_address = f'https://api.openweathermap.org/data/2.5/weather?q=Sudbury&appid={weather_api}'
json_data = requests.get(api_address).json()


def temp():
    temperature = round(json_data["main"]["temp"]-273,1)
    return temperature


def des():
    description= json_data["weather"][0]["description"]
    return description

print(temp())