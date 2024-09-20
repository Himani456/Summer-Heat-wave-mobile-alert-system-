import requests

class Weather:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_current_temperature(self, location):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            return data['main']['temp']
        else:
            print("Error:", data.get("message", "Unknown error"))
            return None
          
