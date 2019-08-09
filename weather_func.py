import pyowm

def get_tempereture(api_key, place_name):
    try:
        owm = pyowm.OWM(api_key)
        observation = owm.weather_at_place(place_name[12:])
        weather = observation.get_weather()
        tempereture = weather.get_temperature('celsius').get('temp')
    except:
        tempereture = None
    return(tempereture)
def get_wind(api_key, place_name):
    try:
        owm = pyowm.OWM(api_key)
        observation = owm.weather_at_place(place_name[15:])
        weather = observation.get_weather()
        tempereture = weather.get_wind().get('speed')
    except:
        tempereture = None
    return(tempereture)
def get_details(api_key, place_name):
    try:
        owm = pyowm.OWM(api_key)
        observation = owm.weather_at_place(place_name[17:])
        weather = observation.get_weather()
        tempereture = weather.get_detailed_status()
    except:
        tempereture = None
    return(tempereture)