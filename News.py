import requests
api_address='https://newsapi.org/v2/top-headlines?country=ca&apiKey=97850604ddce408fb61e3f4b8268c429'
json_data = requests.get(api_address).json()
ar=[]
def news():
    for i in range(3):
        ar.append("number"+str(i+1)+json_data["articles"][i]["title"]+".")
    return ar

