# use open weather map service
import pyowm
owm = pyowm.OWM("") # paste your Open Weather key in the quotes

def weather_at_place(place):
  # returns weather object
  # documentation for what you can do with it:
  # https://pyowm.readthedocs.io/en/latest/pyowm.weatherapi25.html#module-pyowm.weatherapi25.weather
  return owm.weather_at_place(place).get_weather()

def temperature(place):
  # temperature in degrees Celsius (int)
  return owm.weather_at_place(place).get_weather().\
    get_temperature(unit='celsius')["temp"]

def wind(place):
  # wind speed (float)
  return owm.weather_at_place(place).get_weather().\
    get_wind()["speed"]

def clouds(place):
  # cloud cover percentage (int)
  return owm.weather_at_place(place).get_weather().\
    get_clouds()

status = {
  "clouds": "cloudy",
  "drizzle": "drizzly", 
  "rain": "rainy", 
  "thunderstorm": "stormy",
  "snow": "snowy",
  "mist": "misty"
}

def description(place):
  # possible values
  # clear, clouds, rain, thunderstorm, snow, mist
  d = owm.weather_at_place(place).get_weather().\
    get_status().lower()
  return status.get(d, d)