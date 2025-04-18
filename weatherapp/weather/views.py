import requests
from django.shortcuts import render

def index(request):
    if request.method == "POST":
        city = request.POST.get("city")
    else:
        city = ""
        
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    api_key = "f96630d5679a8a918ffed32c47e947b0"
    
    PARAMS = {
        "q": city,
        "appid": api_key,
        "units": "metric",
    }
    
    response = requests.get(url, PARAMS)
    
    if response.status_code == 200:
        data = response.json()
        weather_data = {
            "temp": data["main"]["temp"],
            "pressure": data["main"]["pressure"],
            "humidity": data["main"]["humidity"],
            "speed": data["wind"]["speed"],
            "description": data["weather"][0]["description"],
            "name": data["name"]
        }
    else:
        data = None
    
    return render(request, "index.html", { "datas": weather_data, "city": city, })