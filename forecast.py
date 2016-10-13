from requests import request
import json
import time
from collections import defaultdict


def summary_forecast(city):
   request_url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q={0}&mode=json&units=metric&cnt=14' \
                 '&APPID=1118e9ab51c127fd369e917465652fbc'.format(city)
   # get data from server using builded request_url
   response = request('get',request_url)
   json_data = json.loads(response.text)
   #parsing json output

   weathers = json_data['list']
   maximum = max([temp['temp']['max'] for temp in weathers])
   minimum = min([temp['temp']['min'] for temp in weathers])
   fc = [(weather['weather'][0]['main'],time.strftime('%Y-%m-%d',time.localtime(weather['dt']))) for weather in weathers]
   forecast = defaultdict(list)

   for k,v in fc:
       forecast[k].append(v)

   summary = {
       'city':json_data['city']['name'],
       'maximum':maximum,
       'minimum':minimum,
       'forecast':dict(forecast)
   }

   return summary

print('Enter city: ')
city = input()
print(summary_forecast(city))