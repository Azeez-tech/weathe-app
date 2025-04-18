import requests
from django.shortcuts import render

import os




def index(request):
    if request.method == "POST":
        city = request.POST.get("city")
    else:
        city = ""
        
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    api_key = os.getenv("OPENWEATHER_API_KEY")
    
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