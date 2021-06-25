'''
Napisz program wyświetlający pogodę dla wskazanej przez użytkownika lokalizacji.
Skorzystaj z modułu urllib.request, json oraz API MetaWeather.
'''

import json
import urllib.request
from jsonpath_ng import jsonpath, parse


location = input('Podaj lokalizację dla info o pogodzie: ')
woeid_str=''
woeid_query_str='https://www.metaweather.com//api/location/search/?query=' + location
with urllib.request.urlopen(woeid_query_str) as response:
    dane_w_jsonie = response.read()
    #print(dane_w_jsonie)
    woeid_str = json.loads(dane_w_jsonie)[0]['woeid']

consolidated_weather_query_str='https://www.metaweather.com//api/location/' + str(woeid_str)

with urllib.request.urlopen(consolidated_weather_query_str) as response:

    json_data = json.loads(response.read())
    weather_state_name = parse('$.consolidated_weather[0].weather_state_name').find(json_data)[0].value
    applicable_date = parse('$.consolidated_weather[0].applicable_date').find(json_data)[0].value
    print(f'Pogoda na {applicable_date} dla {location}: {weather_state_name}')

    min_temp = parse('$.consolidated_weather[0].min_temp').find(json_data)[0].value
    print(f'Min Temp: {round(min_temp,1)} C')

    max_temp = parse('$.consolidated_weather[0].max_temp').find(json_data)[0].value
    print(f'Max Temp: {round(max_temp,1)} C')

    wind_direction_compass = parse('$.consolidated_weather[0].wind_direction_compass').find(json_data)[0].value
    print(f'Kierunek wiatru: {wind_direction_compass}')

    wind_speed = parse('$.consolidated_weather[0].wind_speed').find(json_data)[0].value
    print(f'Prędkość wiatru: {round(wind_speed * 1.60934,1)} km/h')

    air_pressure = parse('$.consolidated_weather[0].air_pressure').find(json_data)[0].value
    print(f'Ciśnienie: {air_pressure} hPa')

    humidity = parse('$.consolidated_weather[0].humidity').find(json_data)[0].value
    print(f'Wilgotność: {humidity} %')
