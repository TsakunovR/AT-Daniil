from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class SupportPageLocators:
    WINDOW_SUP = (By.XPATH,'//*[@class="support-chat__kmsu6"]//*[@class="button__tndfc button-icon__tndfc"]')


class SupportPageHelper(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__check_page()


    def __check_page(self):
        self.findElement(SupportPageLocators.WINDOW_SUP)





    def click_win_sup(self):
        win_sup = self.findElement(SupportPageLocators.WINDOW_SUP)
        win_sup.click()



