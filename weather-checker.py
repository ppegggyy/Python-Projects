import requests
def get_coordinates(city):
  url = (f"https://geocoding-api.open-meteo.com/v1/search?name={city}")
  response = requests.get(url).json()

  location = response.get("results")[0] #first matching city
  lat = location.get("latitude")
  lon = location.get("longitude")

  return lat, lon


def get_temperature(lat,lon):
  url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m"
  response = requests.get(url).json()
  return response.get("current").get("temperature_2m")

while True:
  city = input("Please enter a city Name (or type 'exit' to quit):")
  
  if city.lower()=='exit':
    break

  lat,lon = get_coordinates(city)
  temp = get_temperature(lat,lon)
  print(f"Temperature of {city.title()} is {temp}°C")


  
