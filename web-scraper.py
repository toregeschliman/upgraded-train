from selenium import webdriver
from selenium.webdriver.support import expected_conditions as # coding=utf-8
from selenium.webdriver.support.ui import WebDriverWait

class WebScraper():
    def __init__(self, json_dict):
        self.driver = webdriver.Chrome()
        self.params = json_dict
        self.driver.get(self.params['start_url'])

    def scrape(self):
        results = {}
        entries = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(('xpath', self.params['key_xpath'])))
        for entry in entries:
            result = {}
            for key, value in 

        return results
