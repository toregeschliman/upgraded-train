from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.desired_capabilities import DesiredCapabilities

class WebScraper():
    def __init__(self, json_dict):
        self.driver = webdriver.Remote(
            command_executor="http://selenium-remotewebdriver-hub-node:4444/wd/hub",
            desired_capabilities=DesiredCapabilities.CHROME
        )
        self.params = json_dict

    def scrape(self):
        results = {}
        for url_post in self.params['start_url_post']:
            self.driver.get(self.params['start_url'] + url_post)
            entries = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(('xpath', self.params['key_xpath'])))
            for entry in entries:
                result = {}
                for key in self.params['business_data']:
                    result[key] = entry.find_element_by_xpath(self.params['business_data'][key]).text
                results[url_post + str(entries.index(entry))] = result
        self.driver.quit()
        return results
