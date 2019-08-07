import pyowm

def get_tempereture(api_key, place_name):
    try:
        owm = pyowm.OWM(api_key)
        observation = owm.weather_at_place(place_name)
        weather = observation.get_weather()
        tempereture = weather.get_temperature('celsius').get('temp')
    except:
        tempereture = None
    return(tempereture)