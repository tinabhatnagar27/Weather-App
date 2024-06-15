import tkinter as tk
from tkinter import messagebox
import requests

# Replace 'your_api_key_here' with your actual OpenWeatherMap API key
API_KEY = 'ecad6995bbd8f91b8b008cd2a4721c81'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    try:
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'  # Use 'imperial' for Fahrenheit
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data['cod'] != 200:
            raise Exception(data['message'])

        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
        return weather
    except Exception as e:
        messagebox.showerror('Error', str(e))
        return None

def show_weather():
    city = city_entry.get()
    if city:
        weather = get_weather(city)
        if weather:
            result_label['text'] = (
                f"City: {weather['city']}\n"
                f"Temperature: {weather['temperature']} °C\n"
                f"Description: {weather['description'].capitalize()}"
            )
            # To show the weather icon, download it and display in the GUI
            # This part is optional and requires additional code
    else:
        messagebox.showwarning('Input Error', 'Please enter a city name')

# Setting up the main application window
app = tk.Tk()
app.title('Weather App')

# Create the GUI elements
city_label = tk.Label(app, text='Enter city:')
city_label.pack()

city_entry = tk.Entry(app)
city_entry.pack()

get_weather_button = tk.Button(app, text='Get Weather', command=show_weather)
get_weather_button.pack()

result_label = tk.Label(app, text='', justify='left')
result_label.pack()

# Run the main event loop
app.mainloop()