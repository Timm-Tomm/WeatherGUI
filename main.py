from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path

import WeatherFuncs
import gui

#List of weather codes supplied by tomorrow.io
codes =  {
      "0": "Unknown", "1000": "Clear, Sunny", "1100": "Mostly Clear", "1101": "Partly Cloudy", "1102": "Mostly Cloudy", "1001": "Cloudy",
      "2000": "Fog", "2100": "Light Fog", "4000": "Drizzle", "4001": "Rain", "4200": "Light Rain", "4201": "Heavy Rain",
      "5000": "Snow", "5001": "Flurries", "5100": "Light Snow", "5101": "Heavy Snow",
      "6000": "Freezing Drizzle", "6001": "Freezing Rain", "6200": "Light Freezing Rain", "6201": "Heavy Freezing Rain",
      "7000": "Ice Pellets", "7101": "Heavy Ice Pellets", "7102": "Light Ice Pellets",
      "8000": "Thunderstorm"
    }


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\tcoll\WeatherGUI\WeatherGUI\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def main():
    #Initialize Window
    window = Tk()

    window.geometry("1440x1080")
    window.configure(bg = "#DDDDDD")

    canvas = Canvas(
    window,
    bg = "#DDDDDD",
    height = 1080,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )
    gui.base(canvas)
    
    gui.show_facts(canvas)

    gui.show_days(canvas)

    cur = WeatherFuncs.get_current_weather(64015)
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

    #Current picture
    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    CurrentCon = canvas.create_image(
        125,
        125,
        image=image_image_4
    )

    #Fourth Day Picture
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    Day4Pic = canvas.create_image(
        1147.0,
        787.0,
        image=image_image_1
    )

    #Third Day Picture
    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    Day3Pic = canvas.create_image(
        787,
        787.0,
        image=image_image_2
    )

    #Second Day Picture
    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    Day2Pic = canvas.create_image(
        427,
        787.0,
        image=image_image_3
    )

    #First Day Picture
    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    Day1Pic = canvas.create_image(
        67,
        787.0,
        image=image_image_5
    )

    #hour = WeatherFuncs.get_hourly_forecast(64015)
    #hist = WeatherFuncs.get_History()

    window.resizable(False, False)
    window.mainloop()

if __name__ == "__main__":
    main()