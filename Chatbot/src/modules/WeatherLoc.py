import geocoder
import requests
import os
import dotenv

dotenv.load_dotenv()


class LoctWeatherAPI:
    def __init__(self):
        self.api_key = os.environ.get("WEATHER_API_KEY")
        if not self.api_key:
            raise ValueError("WEATHER_API_KEY is missing in environment variables")

    def get_current_location(self):
        
        location = requests.get('http://ipinfo.io/json')
        g = geocoder.ip('me')
        if not g.ok or not g.latlng:
            raise ValueError("Unable to fetch location from IP")
        
        lat, long = g.latlng
        userCountry = g.country if g.country else "Unknown"
        userCity = g.city if g.city else "Unknown"
        userAddress = g.address if g.address else "Unknown"

        return [lat, long, userCity, userCountry, userAddress]



    def get_current_weather(self, loc):
        api_key = os.environ.get("WEATHER_API_KEY_2")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={loc}&appid={api_key}&units=metric"
        res = requests.get(url).json()
        wether_data = [res['weather'][0]['description'], res['main']['temp']]
        return wether_data


# test
# ob = LoctWeatherAPI()
# print(ob.get_current_location())
# print(ob.get_current_weather(ob.get_current_location()[2]))
