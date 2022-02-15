# OpenWeather-Wrapper
This is a wrapper for the OpenWeather API. Requires an OpenWeather API token.

OpenWeather Docs: https://openweathermap.org/api

Example Usage:


Weather = Wrapper("token") # Initializes a Wrapper


Weather.get() # Returns raw weather data dictionary

Weather.update() # Updates cached data, subsequently updates all other information

Weather.setCoords(lat, lon) # Updates cached coordinates


Weather.getTemp() # Returns "temperature" and "feels like"

Weather.getPressure() # Returns "pressure"

Weather.getHumidity() # Returns "humidity"

Weather.getLocation() # Returns Country initials and City name
