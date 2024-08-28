import requests
from bs4 import BeautifulSoup

#API call to tomorrow.io for current weather data
#Requires the location as a parameter to search on
def get_current_weather(location):
    URL = "https://api.tomorrow.io/v4/weather/realtime?location={}%20US&units=imperial&apikey=eMQs1BYAUAZIDiEdTUMRvMve815lXnqm".format(location)
    data = requests.get(URL) 
    return data.json()

#API call to tomorrow.io for forecast data
#This API cannot use the zip code but will accept latitude and longitude (in that order specifically)
def get_daily_forecast(lon, lat):
    URL = "https://api.tomorrow.io/v4/timelines?apikey=eMQs1BYAUAZIDiEdTUMRvMve815lXnqm"
    payload = {
    "location": "{}, {}".format(lat, lon),
    "fields": ["temperature", "temperatureApparent", "humidity", "weatherCode"],
    "units": "imperial",
    "timesteps": ["1d"],
    "startTime": "now",
    "endTime": "nowPlus4d",
    "timezone": "auto"
    }
    headers = {
    "accept": "application/json",
    "Accept-Encoding": "gzip",
    "content-type": "application/json"
    }
    data = requests.post(URL, json=payload, headers=headers)
    return data.json()

#Get "This Day in Weather History" data from weather.gov
def get_History():
    r = requests.get("https://www.weather.gov/eax/wxhistory")
    soup = BeautifulSoup(r.content, 'html.parser')
    content = soup.find_all('tr')
    results = ""
    for line in content:
        results += line.get_text().replace('\n', '').replace('\xa0', '') + '\n\n'
    return results

#API call to tomorrow.io for hourly temperature over the next 6 hours
#This API cannot use the zip code but will accept latitude and longitude (in that order specifically)
def get_Hourly(lon, lat):
    URL = "https://api.tomorrow.io/v4/timelines?apikey=eMQs1BYAUAZIDiEdTUMRvMve815lXnqm"
    payload = {
    "location": "{}, {}".format(lat, lon),
    "fields": ["temperature"],
    "units": "imperial",
    "timesteps": ["1h"],
    "startTime": "now",
    "endTime": "nowPlus6h",
    "timezone": "auto"
    }
    headers = {
    "accept": "application/json",
    "Accept-Encoding": "gzip",
    "content-type": "application/json"
    }
    response = requests.post(URL, json=payload, headers=headers)
    data = response.json()
    hour1Temp = float(data["data"]["timelines"][0]["intervals"][0]["values"]["temperature"])
    hour2Temp = float(data["data"]["timelines"][0]["intervals"][1]["values"]["temperature"])
    hour3Temp = float(data["data"]["timelines"][0]["intervals"][2]["values"]["temperature"])
    hour4Temp = float(data["data"]["timelines"][0]["intervals"][3]["values"]["temperature"])
    hour5Temp = float(data["data"]["timelines"][0]["intervals"][4]["values"]["temperature"])
    hour6Temp = float(data["data"]["timelines"][0]["intervals"][5]["values"]["temperature"])

    points = [hour1Temp, hour2Temp, hour3Temp, hour4Temp, hour5Temp, hour6Temp, hour6Temp]
    return points

if __name__ == "__main__":
    print(get_History())