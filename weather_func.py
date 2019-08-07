import pyowm

def get_tempereture(place_name):
    try:
        owm = pyowm.OWM(' ') #здесь ключ от API
        observation = owm.weather_at_place(place_name)
        weather = observation.get_weather()
        tempereture = weather.get_temperature('celsius').get('temp')
    except:
        tempereture = None
    return(tempereture)