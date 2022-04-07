from tkinter import *
import tkinter as tk
# from geopy.geocoders import Nominatim
# from tkinter import ttk, messagebox
# from timezonefinder import TimezoneFinder
# from datetime import datetime
# import requests
# import pytz

root=Tk()
root.title('Weather App')
root.geometry("600x400")
root.resizable(False, False)

root.mainloop()

# Search_image = PhotoImage(file='search.png')
# myimage = Label(image=Search_image)
# myimage.place(x=0, y=0)

textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg='red', border=0, fg='white')
textfield.place(x=10, y=10)
textfield.focus()


from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser
import requests

url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']

def get_weather(city):
  result = requests.get(url.format(city, api_key))
  if result:
    # print(result.content)
    json = result.json()
    city = json['name']
    country = json['sys']['country']
    temp_kelvin = json['main']['temp']
    temp_celsius = temp_kelvin - 273.15
    temp_farenheit = (temp_kelvin - 273.15) * 9 /5 + 32
    weather = json['weather'][0]['main']
    final = (city, country, temp_celsius, temp_farenheit, weather)
    return final
  else:
    print('Not found')

print(get_weather('Tashkent'))

def search():
  city = city_text.get()
  weather = get_weather(city)
  if weather:
    location_lbl['text'] = '{}, {}'.format(weather[0], weather[1])
    temp_lbl['text'] = '{:.2f}°C, {:.2f}°F'.format(weather[2], weather[3])
    weather_lbl['text'] = weather[4]
  else:
    messagebox.showerror('Error', 'Cannot find city {}'.format(city))

app = Tk()
app.title('Weather App')
app.geometry('400x250')

city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

search_btn = Button(app, text='Search weather', width=12, command=search)
search_btn.pack()

location_lbl = Label(app, text=' ', font=('bold', 20))
location_lbl.pack()

image = Label(app, bitmap='')
image.pack()

temp_lbl = Label(app, text='')
temp_lbl.pack()

weather_lbl = Label(app, text='')
weather_lbl.pack()

app.mainloop()