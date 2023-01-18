from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = OWM('6d00d1d4e704068d70191bad2673e0cc')
mgr = owm.weather_manager()

place = input('Введите в каком городе/стране?: ')

observation = mgr.weather_at_place(place)
w = observation.weather

detailed_status = w.detailed_status
temp = w.temperature('celsius')["temp"]

print('В городе' +  place  +  'сейчас'+ str(detailed_status))
print('Температура сейчас в районе' + str(temp))
