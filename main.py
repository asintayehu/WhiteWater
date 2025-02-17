import requests
import json
import math
import psycopg2

def convert_to_f(temp):
    return (temp * 9/5) + 32

# api key: 5z9CQ7slmvalWcMSxJQOj2qlDQB7nB1c

api_key = "5z9CQ7slmvalWcMSxJQOj2qlDQB7nB1c"

location = input("Enter city: ")

url = f'https://api.tomorrow.io/v4/weather/realtime?location={location}&apikey={api_key}'

headers = { "accept": "application/json" }

response = requests.get(url, headers=headers)

json_data = response.json()

temperature = str(round(convert_to_f(json_data["data"]["values"]["temperature"])))
humidity = json_data["data"]["values"]["humidity"]
wind = json_data["data"]["values"]["windGust"]

print("\nWeather in " + location + ": ")
print("Temp: " + temperature)
print("Humidity: " + str(humidity) + "%")
print("Wind: " + str(math.ceil(wind)))