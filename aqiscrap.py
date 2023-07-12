import requests
from bs4 import BeautifulSoup
import mysql.connector 
obj=mysql.connector.connect(host="localhost",user="root",passwd="saiisking1")

def get_aqi():
    url = 'https://aqicn.org/city/india/hyderabad/central-university/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    aqi_element = soup.find('div', {'class': 'aqivalue'})

    if aqi_element:
        aqi = aqi_element.text.strip()
        level = get_aqi_level(int(aqi))
        print(f"Current AQI in Hyderabad: {aqi} ({level})")
    else:
        print("Unable to retrieve AQI data.")

def get_aqi_level(aqi):
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Moderate"
    elif aqi <= 150:
        return "Unhealthy for Sensitive Groups"
    elif aqi <= 200:
        return "Unhealthy"
    elif aqi <= 300:
        return "Very Unhealthy"
    else:
        return "Hazardous"

    
if __name__ == "__main__" :
    
    get_aqi()
