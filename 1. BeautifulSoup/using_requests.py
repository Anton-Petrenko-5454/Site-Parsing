from bs4 import BeautifulSoup
import requests

url = 'https://yandex.ru/pogoda/saint-petersburg?lat=60.005343&lon=30.401018'

"""
    requests - используем, когда страница не формируется динамически в процессе работы сайта
"""

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

print(soup.prettify())
