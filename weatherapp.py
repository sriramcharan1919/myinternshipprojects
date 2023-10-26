import requests

def get_weather_data(city):
    api_key = "your api key" 
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    try:
        response = requests.get(base_url, params={"q": city, "appid": api_key})
        response.raise_for_status()  # Raise an exception if request is not successful
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {str(e)}")
        return None

def display_weather_data(weather_data):
    if weather_data is not None:
        print(f"Weather for {weather_data['name']}:")
        print(f"Temperature: {weather_data['main']['temp']} K")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Weather conditions: {weather_data['weather'][0]['description']}")
    else:
        print("No weather data available.")

def main():
    city = input("Enter a city name: ")
    weather_data = get_weather_data(city)
    display_weather_data(weather_data)

if __name__ == "__main__":
    main()