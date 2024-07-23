from tkinter import *
import requests
import json
from datetime import datetime

#Initialize Window
root =Tk()
root.geometry("400x400") #size of the window by default
root.resizable(0,0) #to make the window size fixed
#title of our window
root.title("Weather App - AskPython.com")