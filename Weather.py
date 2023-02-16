import requests
api_address='https://api.openweathermap.org/data/2.5/weather?q=Sudbury&appid=cefeb2855f824dd9383c721096c4638f'
json_data = requests.get(api_address).json()

def temp():
    temperature = round(json_data["main"]["temp"]-273,1)
    return temperature
def des():
    description= json_data["weather"][0]["description"]
    return description
print(temp())