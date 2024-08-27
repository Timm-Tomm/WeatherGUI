# WeatherGUI
Python-based GUI app for weather built from Tkinter. The app continually displays weather information for the provided zip code, re-opening the screen and refreshing the data every 5 minutes. 

# Current Weather
There is a container with current weather data pulled from [tomorrow.io](https://www.tomorrow.io/). This data includes temperature, wind, humidity, precipitation, etc.

# Hourly Temperature Forecast
In the center-left of the screen, there is a line graph of the temperature forecasted over the next 6 hours. Coming from [tomorrow.io](https://www.tomorrow.io/).

# Forecast
There is a container at the bottom of the screen that displays the forecast for the next 4 days at the current hour. This information also comes from [tomorrow.io](https://www.tomorrow.io/).

# Weather History
On the right side of the screen resides a container for local and national historical facts about the weather on the current day. For example, May 20 could have notes about the Moore, Oklahoma tornado from 2013. There could be highest/lowest temperatures on record for the day or any other historical data. This data comes from https://www.weather.gov/eax/wxhistory. Unfortunately, the local history version is only for Kansas City, MO as other weather stations do not supply the same style of local weather history. 

# Example from zip code 64015
![image](https://github.com/user-attachments/assets/82992a32-d98a-460d-9394-bd8972fe72b9)
