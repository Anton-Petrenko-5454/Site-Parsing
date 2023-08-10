from bs4 import BeautifulSoup
from selenium import webdriver

# Настройка опции, которая позволяет работать с виртуальным браузером не открывая его.
options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(options=options)

url = 'https://www.soccer.ru/matches-list/'

driver.get(url)

# Создание экземпляра BeautifulSoup для парсинга сайта
soup = BeautifulSoup(driver.page_source, 'html.parser')

driver.quit()

"""
    Методы BeautifulSoup
    Методы могут возвращать PageElement или просто текст.
    
    find(<имя тега для поиска>, class_=<значение класса для поиска>) - метод для поиска элемента на странице по критериям. 
                                                                       Возвращается первый подходящий элемент.
    
    find_all(<имя тега для поиска>, class_=<значение класса для поиска>) - метод, возвращающий все подходящие элементы.
    
    
    Методы PageElement
    find_next(<имя тега для поиска>, class_=<значение класса для поиска>) - метод, возвращающий первый подходящий элемент.
    
    select(<css-селектор>) - метод, возращающий множество тэгов (Tag), подходящих по критерию
    
    Свойства элементов Tag
    .string - возвращает текст элемента
    
    Также, свойства могут возвращать PageElement, к которым можно повторно применять методы.
    
"""

content = soup.find('div', class_='view-content-matches')

all_matches = content.find_all('div', class_='match')

for match in all_matches:
    if match.find_next('span', class_='not-online').string == 'матч завершен':
        home_name = match.find_next('tr', class_='home-row').select('.team-name a')[0].select
        home_score = match.find_next('tr', class_='home-row').select('.score')[0].string

        visit_name = match.find_next('tr', class_='visit-row').select('.team-name a')[0].string
        visit_score = match.find_next('tr', class_='visit-row').select('.score')[0].string

        print(f'{home_name}-{visit_name}\t({home_score}:{visit_score})')