from tkinter import *
import requests
from PIL import Image, ImageTk
import time

def getweather(root):
    city = textfield.get()
    #api = "http://dataservice.accuweather.com/currentconditions/v1/?" + city + "apikey=235771616206d793597a5772fc3105ee"
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + " &appid=235771616206d793597a5772fc3105ee"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Max Temp:" + str(max_temp) + "\n" + "Min Temp:" + str(min_temp)+ "\n" + "Pressure:" \
                 + str(pressure) + "\n" + "Humidity:" + str(humidity) + "\n" +  "Wind speed: " + str(wind)

    label1.config(text = final_info)
    label2.config(text = final_data)

root= Tk()
root.geometry("600x500")
root.title("Weather app")

f = ("poppins", 15, "bold")
t = ("popins", 35, "bold")

textfield = Entry(root, font=t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>', getweather)

label1 = Label(root,font=t)
label1.pack()
label2 = Label(root, font=f)
label2.pack()

root.mainloop()
