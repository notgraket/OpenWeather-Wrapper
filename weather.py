# @notgraket - github
# OpenWeather API Wrapper
# Created: 2-14-2022

import requests

class Cache:
    def __repr__(self):
        return "<class 'weather.Cache'>"
        
        
    def __init__(self):
        self.cache = {}
    

    def put(self, key : str, value):
        """Adds an item to the cache"""
        self.cache[key] = value
            
    
    def get(self, key : str):
        """Returns a value from the cache"""
        return self.cache[key]
    

    def remove(self, key : str):
        """Removes a value from the cache"""
        del self.cache[key]
    

    def first(self):
        """Returns the first key of the cache"""
        return next(iter(self.cache))
    

    def last(self):
        """Returns the last key of the cache"""
        return next(reversed(self.cache))



    
    
class Wrapper:
    def __repr__(self):
        return "<class 'weather.Wrapper'>"


    def __init__(self, openweather_token):
        self.Cache = Cache()

        self.Cache.put(key = "token", value = openweather_token)

        self.Cache.put(
            key = "ipaddress", 
            value = requests.get("https://api.ipify.org?format=json").json()["ip"]
        )

        ipaddress = self.Cache.get("ipaddress")
        self.Cache.put(
            key = "geoinfo", 
            value = requests.get(f"http://ip-api.com/json/{ipaddress}?fields=192").json()
        )

        self.Cache.put(
            key = "latlon", 
            value = (
                self.Cache.get("geoinfo")["lat"], 
                self.Cache.get("geoinfo")["lon"]
            )
        )

        self.Cache.put("weather_data", self.get())


    def get(self) -> dict:
        """Returns weather data"""
        lat, lon = self.Cache.get("latlon")
        token = self.Cache.get("token")
        return requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={token}&units=imperial").json()
    
    
    def set_coords(self, lat : float, lon : float):
        """Updates cached coordinates"""
        self.Cache.put("latlon", (lat, lon))

    
    def update(self):
        """Updates all weather information"""
        self.Cache.put("weather_data", self.get())
    

    def get_clouds(self) -> dict:
        """Returns cloud cover description"""
        return {"cloud_cover" : self.Cache.get("weather_data")["weather"]["descripton"]}
    

    def get_temp(self) -> dict:
        """Returns temperature information"""
        return {
            "temperature" : self.Cache.get("weather_data")["main"]["temp"],
            "feels_like" : self.Cache.get("main")["feels_like"]
        }
    

    def get_pressure(self) -> dict:
        """Returns barometric pressure"""
        return {"pressure" : self.Cache.get("weather_data")["main"]["pressure"]}
    

    def get_humidity(self) -> dict:
        """Returns humidity"""
        return {"humidity" : self.Cache.get("weather_data")["main"]["humidity"]}
    

    def get_location(self) -> dict:
        return {
            "country" : self.Cache.get("weather_data")["sys"]["country"],
            "city" : self.Cache.get("weather_data")["name"]
        }
    



        
        