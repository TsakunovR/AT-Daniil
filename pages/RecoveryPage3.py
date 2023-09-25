from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class RecoveryPageLocators3:
    SUPPORT = (By.XPATH,'//*[@class="ext-registration_f-support-link button-pro __sec"]')
    WINDOW_SUP = (By.XPATH,'//*[@class="support-chat__kmsu6"]//*[@class="button__tndfc button-icon__tndfc"]')


class RecoveryPageHelper3(BasePage):
    def __check_page(self):
        self.findElement(RecoveryPageLocators3.SUPPORT)
        self.findElement(RecoveryPageLocators3.WINDOW_SUP)


    def click_on_support(self):
        on_sup = self.findElement(RecoveryPageLocators3.SUPPORT)
        on_sup.click()


    def click_win_sup(self):
        win_sup = self.findElement(RecoveryPageLocators3.WINDOW_SUP)
        win_sup.click()



