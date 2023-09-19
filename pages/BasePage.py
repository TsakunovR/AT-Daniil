from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self,driver):
        self.driver = driver

    def findElement(self,locator,time=10):
        return WDW(self.driver,time).until(EC.presence_of_element_located(locator),message=f'Не смогли дождаться элемента {locator}')

    def findElements(self,locator,time=10):
        return WDW(self.driver,time).until(EC.presence_of_all_elements_located(locator),message=f'Не смогли дождаться элемента {locator}')

    def go_to_url(self,url):
        return self.driver.get(url)
