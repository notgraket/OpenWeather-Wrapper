# OpenWeather-Wrapper
This is a wrapper for the OpenWeather API. Requires an OpenWeather API token.

OpenWeather Docs: https://openweathermap.org/api

Example Usage:

Weather = Wrapper(token) # Initiate an instance of Wrapper, automatically caches your position for the OpenWeather api call

Weather.get() # This returns a dictionary with all weather data for your area

Weather.update_coords(lat, lon) # Change coordinates used in "Wrapper.get()"
