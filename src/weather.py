import requests

API_KEY = '1cf213f8baa2ff35a28ee3016a1451fe'

def convertToFarenheit(temperature):
    farenheit = temperature * 1.8 + 32
    return farenheit
    

def getWeather(state):
    params = {
        'access_key': API_KEY,
        'query': state
    }
    api_result = requests.get('http://api.weatherstack.com/current', params)
    response_json = api_result.json()
    data = {
        'state': state,
        'description': response_json['current']['weather_descriptions'],
        'humidity': response_json['current']['humidity'],
        'temperature': convertToFarenheit(response_json['current']['temperature'])
    }
    
    return data