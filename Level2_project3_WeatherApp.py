# Weather App Using OpenWeatherMap API

import requests

API_KEY = "dec7ca3d025149789ca66c229dea11a2"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    try:
        params = {"q": city, "appid": API_KEY, "units": "metric"}
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        
        if response.status_code == 200:
            print(f"\nWeather in {data['name']}, {data['sys']['country']}:")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Weather: {data['weather'][0]['description'].capitalize()}")
            print(f"Humidity: {data['main']['humidity']}%")
            print(f"Wind Speed: {data['wind']['speed']} m/s\n")
        else:
            print(f"Error: {data.get('message', 'Unable to fetch weather')}\n")
    except Exception as e:
        print("Error:", e)

def main():
    print("=== Weather App ===")
    while True:
        city = input("Enter city name (or 'exit' to quit): ").strip()
        if city.lower() == "exit":
            print("Exiting Weather App... Goodbye!")
            break
        get_weather(city)

if __name__ == "__main__":
    main()
