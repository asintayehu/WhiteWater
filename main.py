import pgeocode
import requests

api_key = "e2a92538221d485a56aae5456e317793"

zip_code = input("Enter zip code: ")
nomi = pgeocode.Nominatim('us')
query = nomi.query_postal_code(zip_code)
lat = query["latitude"]
lon = query["longitude"]

x = requests.get("https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={e2a92538221d485a56aae5456e317793}")

print(x)