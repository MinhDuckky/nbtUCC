import requests

endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
apikey = input('Enter API key: ')

print()
print("Weather Forecasting the next 5 days....")
print("--------------------------------------------------")
print()

#Params 
param = {
    "q": "Ha Noi",
    "appid" : apikey,
    "units" : "metric"
}


r = requests.get(endpoint, params = param)

#Json data
data = r.json()

class Forecast:
    def __init__(self, min, max, feel, cloud, humid, weather, wind, date, time):
        self.min = min
        self.max = max
        self.feel = feel
        self.cloud = cloud
        self.humid = humid
        self.weather = weather
        self.wind = wind
        self.date = date
        self.time = time
    def show(self):
        print(f"{self.date} |    {self.time}\n")
        print(f"{self.weather}")
        print(f"Temperature: {self.min} - {self.max}")
        print(f"Feels like: {self.feel}")
        print(f"Clouds: {self.cloud}")
        print(f"Humidity: {self.humid}")
        print(f"Wind: {self.wind}\n\n")

for forecast in data["list"]:
    min = str(forecast["main"]["temp_min"]) + "°C"
    max = str(forecast["main"]["temp_max"]) + "°C"
    feel = str(forecast["main"]["feels_like"]) + "°C"
    cloud = str(forecast["clouds"]["all"]) + "%"
    humid = str(forecast["main"]["humidity"]) + "%"
    weather = str(forecast["weather"][0]["description"]).upper()    
    wind = str(forecast["wind"]["speed"]) + " km/h"
    date_time = str(forecast["dt_txt"]).split()
    date = date_time[0].split("-")[::-1]
    date = "-".join(date)
    time = date_time[1]
    new = Forecast(min, max, feel, cloud, humid, weather, wind, date, time)
    new.show()




    
    
    
