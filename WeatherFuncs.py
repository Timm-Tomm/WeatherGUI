import requests
import json
import main
from datetime import datetime
from bs4 import BeautifulSoup
from string import Template

#API call to tomorrow.io for current weather data
#Requires the location as a parameter to search on
def get_current_weather(location):
    URL = "https://api.tomorrow.io/v4/weather/realtime?location={}%20US&units=imperial&apikey=eMQs1BYAUAZIDiEdTUMRvMve815lXnqm".format(location)
    data = requests.get(URL) 
    return data.json()

#API call to tomorrow.io for forecast data
#Requires the location as a parameter to search on
def get_daily_forecast(location):
    URL = "https://api.tomorrow.io/v4/timelines?apikey=eMQs1BYAUAZIDiEdTUMRvMve815lXnqm"
    payload = {
    "location": "39.029292, -94.274253",
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
            #results += line.get_text()
    return results

if __name__ == "__main__":
    print(get_History())