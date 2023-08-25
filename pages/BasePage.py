from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC

class Basepage:

    def __init__(self,driver):
        self.driver = driver

    def findelemet(self,locator,time=10):
        return WDW(self.driver,time).until(EC.presence_of_element_located(locator),message=f'Не смогли дождаться элемента {locator}')

    def findelemets(self):
        return WDW(self.driver,time).until(EC.presence_of_all_elements_located(locator),message=f'Не смогли дождаться элемента {locator}')

    def go_to_url(self,url):
        return self.driver.get(url)
