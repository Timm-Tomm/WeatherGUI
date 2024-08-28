from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path

import WeatherFuncs, time, gui, tksvg, pgeocode

#List of weather codes supplied by tomorrow.io
codes =  {
      "0": "Unknown", "1000": "Clear, Sunny", "1100": "Mostly Clear", "1101": "Partly Cloudy", "1102": "Mostly Cloudy", "1001": "Cloudy",
      "2000": "Fog", "2100": "Light Fog", "4000": "Drizzle", "4001": "Rain", "4200": "Light Rain", "4201": "Heavy Rain",
      "5000": "Snow", "5001": "Flurries", "5100": "Light Snow", "5101": "Heavy Snow",
      "6000": "Freezing Drizzle", "6001": "Freezing Rain", "6200": "Light Freezing Rain", "6201": "Heavy Freezing Rain",
      "7000": "Ice Pellets", "7101": "Heavy Ice Pellets", "7102": "Light Ice Pellets",
      "8000": "Thunderstorm"
    }

#Weather codes relating to different pictures supplied by Tomorrow.io
images = {
      "0": "clear_day.svg", "1000": "clear_day.svg", "1100": "mostly_cloudy.svg", "1101": "partly_cloudy_day.svg", "1102": "mostly_cloudy.svg", "1001": "cloudy.svg",
      "2000": "fog.svg", "2100": "fog_light.svg", "4000": "drizzle.svg", "4001": "rain.svg", "4200": "rain_light.svg", "4201": "rain_heavy.svg",
      "5000": "snow.svg", "5001": "flurries.svg", "5100": "snow_light.svg", "5101": "snow_heavy.svg",
      "6000": "freezing_drizzle.svg", "6001": "freezing_rain.svg", "6200": "freezing_rain_light.svg", "6201": "freezing_rain_heavy.svg",
      "7000": "ice_pellets.svg", "7101": "ice_pellets_heavy.svg", "7102": "ice_pellets_light.svg",
      "8000": "tstorm.svg"
}

#Defining a path for Tkinter to follow when pulling images
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"tomorrow-weather-codes/V1_icons/color")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

'''This function pulls all of the relevant data from other files and displays it to users via Tkinter.
It destroys the current window and repopulates the data every 5 minutes.''' 
def main():
    #Get user defined location so it isn't hard-coded and can be changed
    location = input("Enter zip code: ")

    #Takes the entered zip code and find the latitude and longitude for one of the functions
    nomi = pgeocode.Nominatim("us")
    latlon = nomi.query_postal_code(location)
    lon = str(latlon['longitude'])
    lat = str(latlon['latitude'])
    
    while True:
        #Initialize Tkinter Window
        window = Tk()
        window.geometry("1440x1080")
        canvas = Canvas(
        window,
        bg = "#000030",
        height = 1080,
        width = 1440,
        bd = 0,
        highlightthickness = 0,
        relief = "sunken"
        )

        #Build out the basis of the GUI before data is added to it
        gui.base(canvas)
        
        #Pull the weather history for the day from the National Weather Service
        history = WeatherFuncs.get_History()
        gui.show_facts(canvas, history)

        #Build out current weather
        cur = WeatherFuncs.get_current_weather(location)
        temp = str(cur["data"]["values"]["temperature"])
        rf = str(cur["data"]["values"]["temperatureApparent"])
        humid = str(cur["data"]["values"]["humidity"])
        windS = str(cur["data"]["values"]["windSpeed"])
        windD = cur["data"]["values"]["windDirection"]
        precip = str(cur["data"]["values"]["precipitationProbability"])
        pressure = str(cur["data"]["values"]["pressureSurfaceLevel"])
        weatherCode = str(cur["data"]["values"]["weatherCode"])
        curCode = codes[weatherCode]
        gui.show_cur(canvas, temp, rf, humid, windS, windD, precip, pressure, curCode)

        #Build out the daily forecast
        days = WeatherFuncs.get_daily_forecast(lon, lat)
        day1Temp = str(days["data"]["timelines"][0]["intervals"][0]["values"]["temperature"])
        day1RF = str(days["data"]["timelines"][0]["intervals"][0]["values"]["temperatureApparent"])
        day1Humid = str(days["data"]["timelines"][0]["intervals"][0]["values"]["humidity"])
        day1Code = str(days["data"]["timelines"][0]["intervals"][0]["values"]["weatherCode"])
        day2Temp = str(days["data"]["timelines"][0]["intervals"][1]["values"]["temperature"])
        day2RF = str(days["data"]["timelines"][0]["intervals"][1]["values"]["temperatureApparent"])
        day2Humid = str(days["data"]["timelines"][0]["intervals"][1]["values"]["humidity"])
        day2Code = str(days["data"]["timelines"][0]["intervals"][1]["values"]["weatherCode"])
        day3Temp = str(days["data"]["timelines"][0]["intervals"][2]["values"]["temperature"])
        day3RF = str(days["data"]["timelines"][0]["intervals"][2]["values"]["temperatureApparent"])
        day3Humid = str(days["data"]["timelines"][0]["intervals"][2]["values"]["humidity"])
        day3Code = str(days["data"]["timelines"][0]["intervals"][2]["values"]["weatherCode"])
        day4Temp = str(days["data"]["timelines"][0]["intervals"][3]["values"]["temperature"])
        day4RF = str(days["data"]["timelines"][0]["intervals"][3]["values"]["temperatureApparent"])
        day4Humid = str(days["data"]["timelines"][0]["intervals"][3]["values"]["humidity"])
        day4Code = str(days["data"]["timelines"][0]["intervals"][3]["values"]["weatherCode"])
        Code1 = codes[day1Code]
        Code2 = codes[day2Code]
        Code3 = codes[day3Code]
        Code4 = codes[day4Code]
        gui.show_days(canvas, day1Temp, day2Temp, day3Temp, day4Temp, day1RF, day2RF, day3RF, day4RF, day1Humid, day2Humid, day3Humid, day4Humid, Code1, Code2, Code3, Code4)
        
        #Generate points for the hourly temperature forecast
        points = WeatherFuncs.get_Hourly(lon, lat)
        gui.show_hourly(canvas, points) 

        #Current picture
        #PhotoImage(master=canvas)
        image_image_4 = tksvg.SvgImage(
            file=relative_to_assets(images[weatherCode]))
        image_image_4 = image_image_4.zoom(6, 6)
        CurrentCon = canvas.create_image(
            125,
            125,
            image=image_image_4
        )

        #Fourth Day Picture
        image_image_1 = tksvg.SvgImage(
            file=relative_to_assets(images[day4Code]))
        image_image_1 = image_image_1.zoom(4, 4)
        Day4Pic = canvas.create_image(
            1260.0,
            787.0,
            image=image_image_1
        )

        #Third Day Picture
        image_image_2 = tksvg.SvgImage(
            file=relative_to_assets(images[day3Code]))
        image_image_2 = image_image_2.zoom(4, 4)
        Day3Pic = canvas.create_image(
            900,
            787.0,
            image=image_image_2
        )

        #Second Day Picture
        image_image_3 = tksvg.SvgImage(
            file=relative_to_assets(images[day2Code]))
        image_image_3 = image_image_3.zoom(4, 4)
        Day2Pic = canvas.create_image(
            540,
            787.0,
            image=image_image_3
        )

        #First Day Picture
        image_image_5 = tksvg.SvgImage(
            file=relative_to_assets(images[day1Code]))
        image_image_5 = image_image_5.zoom(4, 4)
        Day1Pic = canvas.create_image(
            170,
            787.0,
            image=image_image_5
        )

        #Credits to tomorrow.io for data and images
        tomorrowPic = PhotoImage(
            file=Path(r"C:\Users\tcoll\WeatherGUI-1\tomorrow-weather-codes\powered-by-tomorrow\Powered_by_Tomorrow-White.png"))
        Pic = canvas.create_image(
            1180,
            40,
            image = tomorrowPic,
        )

        #Show clock and location in the top left
        gui.show_time(canvas, location)
        window.resizable(False, False)
        
        #Resets window and data after 5 minutes
        for i in range(300):
            window.after(1000, window.update())
        window.destroy()

if __name__ == "__main__":
    main()
