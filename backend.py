import requests

API_KEY = '8ba57a6732a06cf6ca72eb87a7a06917'

def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == '__main__':
    print(get_data(place='Guangzhou'))