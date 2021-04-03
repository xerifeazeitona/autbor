#! /usr/bin/env python3
"""
get_open_weather.py - Prints the weather for a location from the CLI
"""

import sys
import json
import requests

APPID = input('Enter API key: ')

# Compute location from command line arguments
if len(sys.argv) < 2:
    print('Usage: ./get_open_weather.py CITY_NAME, 2-LETTER-COUNTRY-CODE')
    sys.exit()
location = ''.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API
url = 'https://api.openweathermap.org/data/2.5/forecast/daily?q='
url += f'{location}&cnt=3&APPID={APPID}'
response = requests.get(url)
response.raise_for_status()
# Uncomment to see the raw JSON text
#print(response.text)

# Load JSON data into a python variable
weather_data = json.loads(response.text)

# Print weather descriptions
w = weather_data['list']
print(f'Current weather in {location}:')
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
print()
