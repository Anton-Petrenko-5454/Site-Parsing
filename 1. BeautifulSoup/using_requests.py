from bs4 import BeautifulSoup
import requests

url = 'https://yandex.ru/pogoda/saint-petersburg?lat=60.005343&lon=30.401018'

"""
    requests - используем, когда страница не формируется динамически в процессе работы сайта
"""

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

all_days=soup.find_all('li', class_='forecast-briefly__day swiper-slide')

for day in all_days:
    name_day=day.find_next('div', class_='forecast-briefly__name').string
    number_day = day.find_next('time', class_='time forecast-briefly__date').string
    weather_day = day.find_next('div', class_='forecast-briefly__condition').string
    middle_temperature_day = day.find_next('div', class_='temp forecast-briefly__temp forecast-briefly__temp_day').string
    night_temperature_day = day.find_next('div', class_='temp forecast-briefly__temp forecast-briefly__temp_night').string
    print(f'{name_day} {number_day} , погода {weather_day} , температура днем достигнет {middle_temperature_day} , а ночью упадет до {night_temperature_day}')


