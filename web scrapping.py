import requests
from bs4 import BeautifulSoup
import pandas as pd
url = 'https://kaggle.com/muthuj7/weather-dataset'
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    temperature = soup.find('span', class_='temperature')
    humidity = soup.find('span', class_='humidity')
    weather_data = {
        'Temperature': temperature,
        'Humidity': humidity
    }
    
    df = pd.DataFrame([weather_data])
    df.to_csv('weather_data.csv', index=False)
    print('Data scraped and saved successfully.')
else:
    print('Failed to retrieve the web page.')
