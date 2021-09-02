# Project - Fetching current weather data

import json
import requests
import sys

'''
API key sourced from https://home.openweathermap.org/api_keys
API key deleted - to run this program, replace the below string with a new key
'''
APPID = '792b8c4d94a7daa8eba47bb5bc4dde90'


# Compute locations from cmd
if len(sys.argv) < 2:
    print("Usage: getOpenWeather.py city_name, 2-letter_country_code")
    sys.exit()

location = ''.join(sys.argv[1:])

# Download JSON from API
url = (
    f"https://api.openweathermap.org/data/2.5/forecast/daily?q={location}&cnt=3&APPID={APPID}")
response = requests.get(url)
response.raise_for_status()

# Print raw JSON text
# print(response.text)

# Load JSON into python variable
weatherData = json.loads(response.text)

# Print weather descriptions
w = weatherData['list']

print(f'Current weather in {location}:')
print(w[0]['weather'][0]['main'], ' - ', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], ' - ', w[1]['weather'][0]['description'])
