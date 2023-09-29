from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class RecoveryPageLocators1:
    NUMBER = (By.XPATH,'//*[@class="ext-registration_stubs"]//*[@data-l="t,phone"]')
    POST = (By.XPATH, '//*[@class="ext-registration_stubs"]//*[@data-l="t,email"]')
    SUPPORT = (By.XPATH,'//*[@class="ext-registration_f-support-link button-pro __sec"]')




class RecoveryPageHelper1(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__check_page()

    def __check_page(self):
        self.findElement(RecoveryPageLocators1.NUMBER)
        self.findElement(RecoveryPageLocators1.POST)
        self.findElement(RecoveryPageLocators1.SUPPORT)

    def click_on_phone(self):
        on_phone = self.findElement(RecoveryPageLocators1.NUMBER)
        on_phone.click()

    def click_on_post(self):
        on_post = self.findElement(RecoveryPageLocators1.POST)
        on_post.click()

    def click_on_support(self):
        on_sup = self.findElement(RecoveryPageLocators1.SUPPORT)
        on_sup.click()









