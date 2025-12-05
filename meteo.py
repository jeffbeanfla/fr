import openmeteo_requests
openmeteo=openmeteo_requests.Client()

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude":26.07,
    "longitude":-80.15,
    "current": ["temperature_2m", "precipitation"],
    "temperature_unit":"fahrenheit",
    }

responses = openmeteo.weather_api(url,params=params)
response = responses[0]
current =response.Current()
current_temperature_2m=current.Variables(0).Value()

print ({current_temperature_2m}),
