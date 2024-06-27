import requests

API_KEY = '8ba57a6732a06cf6ca72eb87a7a06917'

def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    # 拿 list 里的数据
    filter_data = data['list']
    # 每天统计 8个点
    nr_days = 8 * forecast_days
    filter_data = filter_data[:nr_days]
    # if kind == 'Temperature':
    #     # filter_data 中的每一个字典的 main 键下的 temp 值被提取出来，组成一个新的列表
    #     # 比如 filter_data = [20.5, 22.3, 19.8]
    #     filter_data = [dict['main']['temp'] for dict in filter_data]
    # if kind == 'Sky':
    #     filter_data = [dict['weather'][0]['temp'] for dict in filter_data]

    return filter_data

if __name__ == '__main__':
    print(get_data(place='Guangzhou', forecast_days=3))