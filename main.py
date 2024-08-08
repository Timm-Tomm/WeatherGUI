from tkinter import *
import WeatherFuncs
import gui.py

def main():
    #Initialize Window
    root =Tk()
    #root.geometry("1080x720") #size of the window by default
    root.resizable(0,0) #to make the window size fixed
    
    #title of our window


    #cur = WeatherFuncs.get_current_weather(64015)
    #hour = WeatherFuncs.get_hourly_forecast(64015)
    #hist = WeatherFuncs.get_History()
    #print(cur)

    canvas = Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg="#87CEEB")

    #canvas.create_text(300, 50, text=("Temperature: " + str(cur["data"]["values"]["temperature"]) + "°F"), fill="black")
    canvas.pack()
    
    close = Button(canvas, text="Close", command=root.destroy, bg="grey")
    close.place(x=root.winfo_screenwidth()-45, y=5)
    root.wm_attributes('-fullscreen', 'True')
    root.mainloop()

if __name__ == "__main__":
    main()