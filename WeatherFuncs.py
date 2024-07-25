import requests
import json
from datetime import datetime
from bs4 import BeautifulSoup
#API call to tomorrow.io for current weather data
#Requires the location as a parameter to search on
def get_current_weather(location):
    url = "https://api.tomorrow.io/v4/weather/realtime?location={}%20US&units=imperial&apikey=eMQs1BYAUAZIDiEdTUMRvMve815lXnqm".format(location)
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.text

#API call to tomorrow.io for forecast data
#Requires the location as a parameter to search on
def get_hourly_forecast(location):
    url = "https://api.tomorrow.io/v4/weather/forecast?location={}%20US&timesteps=1h&units=imperial&apikey=eMQs1BYAUAZIDiEdTUMRvMve815lXnqm".format(location)
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.text

#Get "This Day in Weather History" data from weather.gov
def get_History():
    r = requests.get("https://www.weather.gov/eax/wxhistory")
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('tbody', class_="boldtype")
    content = s.find_all('tr')
    return content
