from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(options=options)

url = 'https://www.soccer.ru/matches-list/'

driver.get(url)

content = driver.find_element(By.CLASS_NAME, 'view-content-matches')

all_matches = content.find_elements(By.CLASS_NAME, 'match')

for match in all_matches:
    try:
        # TODO: Решить проблему NoSuchElementException
        status = match.find_element(By.CSS_SELECTOR, '.not-online')
        if status is not None and status.text == 'матч завершен':
            home = match.find_element(By.CLASS_NAME, 'home-row')
            visit = match.find_element(By.CLASS_NAME, 'visit-row')

            home_name = home.find_element(By.CLASS_NAME, 'team-name').find_element(By.TAG_NAME, 'a').text
            home_score = home.find_element(By.CLASS_NAME, 'score').text

            visit_name = visit.find_element(By.CLASS_NAME, 'team-name').find_element(By.TAG_NAME, 'a').text
            visit_score = visit.find_element(By.CLASS_NAME, 'score').text

            print(f'{home_name}-{visit_name}\t({home_score}:{visit_score})')
    except Exception as e:
        print(e)

driver.quit()

