
import requests
import json

api_key = "b4fc6870c8dbec2794fecdb496db6d4d"

city = input("Enter city name: ")

fetch_lat_lon_of_city = f"https://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}"

city_data = []

# Getting latitude and longitude of the city provided by the user
try:
    response = requests.get(fetch_lat_lon_of_city)
    if response.status_code==200:
        city_data = response.json()

except requests.exceptions.RequestException as e:
    print ("Request could not be completed.")



for a in city_data:
    city = a["name"].capitalize()
    latitude = a["lat"]
    longitude = a["lon"]
    country= a["country"]

    fetch_weather = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&units=metric&appid={api_key}"

    try:
        response = requests.get(fetch_weather)
        if response.status_code==200:
            json_response = response.json()
            print(f"Weather update in {city}")
            print(f"Temperature: {json_response.get('main').get('temp')} Celsius")
            print(f"Description: {json_response.get('weather')[0].get('description')}")


    except requests.exceptions.RequestException as e:
        print ("Request could not be completed.")

