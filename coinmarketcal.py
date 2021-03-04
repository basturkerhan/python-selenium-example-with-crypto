from selenium import webdriver
from csv import writer
import time

with open('coinEvents.csv','w') as file:
    csv_writer = writer(file)
    driver = webdriver.Chrome()
    driver.get('https://coinmarketcal.com/tr')
    
    def loadEvents():
        cards = driver.find_elements_by_css_selector('.list-card article .card .card__body')
        for card in cards:
            name    = card.find_element_by_css_selector('.card__coins a').text
            title   = card.find_element_by_css_selector('.card__title').text
            date    = card.find_element_by_css_selector('.card__date').text
            desc    = card.find_element_by_css_selector('.box .card__description').text            
            csv_writer.writerow([name,title,date])
                
    while True:
        pagination = driver.find_elements_by_css_selector('.pagination li')
        loadEvents()
        if pagination[-2].text == '>':
            nextPage = pagination[-2].find_element_by_tag_name('a').get_attribute('href')
            driver.get(nextPage)
        else:
            break
    
    driver.close()