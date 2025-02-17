import requests
import pgeocode
import math

nomi = pgeocode.Nominatim('us')

zip_code = input("Enter zip code here: ")

# Fetching latitude and longitude based on zip code
query = nomi.query_postal_code(zip_code)
data = { "lat": query["latitude"], "lon": query["longitude"] }
latitude = str(data["lat"]).strip()
longitude = str(data["lon"]).strip()

# Fetching city name
location = query['place_name']


x = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}8&lon={longitude}&appid={API_KEY}&units=imperial')

weather_data = x.json()

# fetching all relevant info from json
temperature = math.ceil(weather_data['main']['temp'])
feels_like = weather_data['main']['feels_like']
humidity = weather_data['main']['humidity']
wind = weather_data['wind']['speed']
description = weather_data['weather'][0]['main']

# outputting data
print("Temperature is " + str(temperature))
print("Humidity is " + str(humidity))
print("Feels like " + str(feels_like))
print("Wind speed is " + str(wind))
print("It's looking " + str(description).lower() + " outside today")




# Broken code due to inaccurate API

# location = input("Enter city: ")

# url = f'https://api.tomorrow.io/v4/weather/realtime?location={location}&apikey={api_key}'

# headers = { "accept": "application/json" }

# response = requests.get(url, headers=headers)

# json_data = response.json()

# temperature = str(round(convert_to_f(json_data["data"]["values"]["temperature"])))
# humidity = json_data["data"]["values"]["humidity"]
# wind = json_data["data"]["values"]["windGust"]

# print("\nWeather in " + location + ": ")
# print("Temp: " + temperature)
# print("Humidity: " + str(humidity) + "%")
# print("Wind: " + str(math.ceil(wind)))