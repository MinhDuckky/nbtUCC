import requests
import json
import os
import sys


endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
apikey = input('Enter API key: ')


#Params 
param = {
    "q": "Ha Noi",
    "appid" : apikey,
    "units" : "metric"
}


r = requests.get(endpoint, params = param)

#Json data
data = r.json()

    
list = []
for forecast in data["list"]:
    min = str(forecast["main"]["temp_min"]) + "°C"
    max = str(forecast["main"]["temp_max"]) + "°C"
    feel = str(forecast["main"]["feels_like"]) + "°C"
    cloud = str(forecast["clouds"]["all"]) + "%"
    humid = str(forecast["main"]["humidity"]) + "%"
    weather = str(forecast["weather"][0]["description"]).upper()    
    icon = str(forecast["weather"][0]["icon"])   
    wind = str(forecast["wind"]["speed"]) + " km/h"
    date_time = str(forecast["dt_txt"]).split()
    date = date_time[0].split("-")[::-1]
    date = "-".join(date)
    time = date_time[1]
    dict = {
    "min": min,
    "max": max,
    "feel": feel,
    "cloud": cloud,
    "humid": humid,
    "weather": weather,
    "icon": icon,
    "wind": wind,
    "date": date,
    "time": time
    }
    copy = dict.copy()
    list.append(copy)

with open(os.path.join(sys.path[0], "data.json"), "w") as outfile:
    json.dump(list, outfile)




    
    
    
