from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class PolicyLocators:
    TITLE = (By.XPATH,'//*[@class="portlet_h"]')
    QUESTIONS =(By.XPATH,'//*[@class="portlet_h __with-border"]')


class PolicyPageHelper(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__check_page()

    def __check_page(self):
        self.findElement(PolicyLocators.TITLE)
        self.findElement(PolicyLocators.QUESTIONS)








