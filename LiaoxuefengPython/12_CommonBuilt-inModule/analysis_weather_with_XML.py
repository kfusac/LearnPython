# -*- coding:utf-8 -*-

from xml.parsers.expat import ParserCreate
from urllib import request
import json
from datetime import datetime

class WeatherSaxHandler(object):
    city_forecast=dict()
    _forecasts_list=[]
    city_forecast['forecast']=_forecasts_list
    def start_element(self,name,attrs):
        if name=='yweather:location':
            city_forecast['city']=attrs['city']
        if name=='yweather:forecast':
            _forecast={
                'data':str(datetime.strptime(attrs['data'],'%d %b %Y').date()),
                'high':int(attrs['high']),
                'low':int(attrs['low'])
            }
            _forecasts_list.append(_forecast)            
    
    def end_element(self,name):
        pass
    
    def char_data(self,text):
        pass

def parseXml(xml_str):
    # print(xml_str)
    city_forecast=dict()
    _forecasts_list=[]
    class WeatherSaxHandler(object):    
        city_forecast['forecast']=_forecasts_list
        def start_element(self,name,attrs):
            if name=='yweather:location':
                city_forecast['city']=attrs['city']
            if name=='yweather:forecast':
                _forecast={
                    'data':str(datetime.strptime(attrs['date'],'%d %b %Y').date()),
                    'high':int(attrs['high']),
                    'low':int(attrs['low'])
                }
                _forecasts_list.append(_forecast)            
        
        def end_element(self,name):
            pass
        
        def char_data(self,text):
            pass
    
    handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml_str)
    
    
    return city_forecast
    
    # return {
        # 'city': '?',
        # 'forecast': [
            # {
                # 'date': '2017-11-17',
                # 'high': 43,
                # 'low' : 26
            # },
            # {
                # 'date': '2017-11-18',
                # 'high': 41,
                # 'low' : 20
            # },
            # {
                # 'date': '2017-11-19',
                # 'high': 43,
                # 'low' : 19
            # }
        # ]
    # }

# 测试:
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
assert result['city'] == 'Beijing'
print('OK')