import requests
import json

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] != 200:
        return None
    return {
        "city": data["name"],
        "temp": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"]
    }

def display_weather(weather_data):
    if weather_data is None:
        print("Error fetching weather data. Check city name or API key.")
        return
    print(f"Weather in {weather_data['city']}:")
    print(f"Temperature: {weather_data['temp']}°C")
    print(f"Description: {weather_data['description'].capitalize()}")
    print(f"Humidity: {weather_data['humidity']}%")
    print(f"Wind Speed: {weather_data['wind_speed']} m/s")

def main():
    api_key = "YOUR_API_KEY_HERE"
    city = input("Enter city name: ")
    weather_data = get_weather(city, api_key)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
