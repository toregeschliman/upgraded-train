from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
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
            for key in self.params['business_data']:
                result[key] = entry.find_element_by_xpath(self.params['business_data'][key]).text
            results[str(entries.index(entry))] = result
        self.driver.quit()
        return results
