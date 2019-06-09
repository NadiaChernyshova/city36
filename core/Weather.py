import requests

class Weather:
    def generate_url_weather(self):
        return 'http://api.openweathermap.org/data/2.5/weather'


    def __init__(self, api_key):
        self.api_key = api_key
        self.url_weather = self.generate_url_weather()



    def format_data(self):
        s_city = 'Voronezh,RU'
        appid = self.api_key
        try:
            res = requests.get(self.url_weather, params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
            data = res.json()
            return data
        except Exception as e:
            print("Exception (find): ", e)
        

