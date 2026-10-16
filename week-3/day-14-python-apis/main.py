# Day 14 — Python APIs
# Task: Fetch weather data from OpenWeather API using the requests library and environment variables.

import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("API_KEY")

def fetch_data(city):
    # OpenWeather Current Weather Data endpoint
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric" # Gets temperature in Celsius
    }
    
    print(f"Fetching weather data for '{city}'...")
    try:
        response = requests.get(url, params=params)
        
        # Inspect response url and status code as required
        print(f"Request URL: {response.url}")
        print(f"Status Code: {response.status_code}")
        
        response.raise_for_status()
        return response.json()
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the API request: {e}")
        return None

def display_results(data):
    if not data:
        print("No data received.")
        return
        
    # Extracting at least 3 useful pieces of information from the response
    city_name = data.get("name", "Unknown")
    country = data.get("sys", {}).get("country", "")
    weather_desc = data.get("weather", [{}])[0].get("description", "N/A")
    temp = data.get("main", {}).get("temp", "N/A")
    humidity = data.get("main", {}).get("humidity", "N/A")
    
    print(f"\n--- Weather Report for {city_name}, {country} ---")
    print(f"1. Weather Condition: {weather_desc.capitalize()}")
    print(f"2. Temperature: {temp}°C")
    print(f"3. Humidity: {humidity}%")
    print("-" * 40)

def main():
    city = input("Enter city name (e.g., Lagos, London): ")
    data = fetch_data(city)
    if data:
        display_results(data)

if __name__ == "__main__":
    main()