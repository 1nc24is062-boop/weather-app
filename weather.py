import requests

# Replace with your actual API key from https://home.openweathermap.org/api_keys
API_KEY = "0677782f1782801ab9f49755db3b7ebb"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

# Ask user for city
city = input("Enter city name: ")

# Build request URL
url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"

# Make request
response = requests.get(url)
data = response.json()

# Debug: print the whole response if needed
# print(data)

# Check if response contains weather data
if data.get("cod") == 200:
    main = data["main"]
    temperature = main["temp"]
    humidity = main["humidity"]
    weather_desc = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    print(f"\nWeather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {weather_desc}")
    print(f"Wind Speed: {wind_speed} m/s")
else:
    print("Error:", data.get("message", "City not found"))
