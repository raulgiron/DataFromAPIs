import requests
from keys import api_key
import csv

country = 'DO'
city = 'Santo Domingo'
UOM = 'metric'
r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city},{country}&units={UOM}&appid={api_key}')
print(r.status_code)
# print(r.json())
data = r.json()
# print(data['weather'][0]['main'])

weather = data['weather'][0]['main']
temp = data['main']['temp']
wind_speed = data['wind']['speed']

header = ['city', 'country_code', 'weather', 'temp', 'wind_speed']
info = [city, country, weather, temp, wind_speed]

with open('weather.csv', 'w') as f:
    writer = csv.writer(f)
    # write the header.
    writer.writerow(header)
    # write the data.
    writer.writerow(info)
