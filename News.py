import requests
import datetime
import API
news_api = API.news_api
api_address = f'https://newsapi.org/v2/top-headlines?country=ca&apiKey={news_api}'
json_data = requests.get(api_address).json()


def news():
    all_news = ""
    for i in range(3):
        all_news = all_news + "number" + str(i + 1) + json_data["articles"][i]["title"] + ".  "
    return all_news


def get_formatted_date():
    now = datetime.datetime.now()
    day = now.strftime("%d").lstrip('0')
    suffix = get_day_suffix(int(day))
    return now.strftime("%B ") + day + suffix + now.strftime(", %Y")


def get_day_suffix(day):
    if 11 <= day <= 13:
        return 'th'
    else:
        return {1: 'st', 2: 'nd', 3: 'rd'}.get(day % 10, 'th')


def get_current_time():
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")


def return_date():
    return"Today is " + get_formatted_date()


def return_time():
    return"The current time is" + get_current_time()
