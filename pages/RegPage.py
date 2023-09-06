from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class RegPageLocators:
    REGISTRATION = (By.XPATH,'//*[@data-l="t,register"]')
    NUMBER_FIELD = (By.XPATH,'//*[@id="field_phone"]')
    ERROR_NUMBER_PHONE = (By.XPATH,'//*[@class="input-e js-ph-vl-hint"]')
    NEXT = (By.XPATH,'//*[@data-l="t,submit"]')


class RegPageHelper(BasePage):
    def __check_page(self):
            self.findelement(RegPageLocators.REGISTRATION)
            self.findelement(RegPageLocators.ERROR_NUMBER_PHONE)
            self.findelement(RegPageLocators.NUMBER_FIELD)
            self.findelement(RegPageLocators.NEXT)


    def click_reg_button(self):
        reg_button = self.findelement(RegPageLocators.REGISTRATION)
        reg_button.click()


    def click_next_button(self):
        next_button = self.findelement(RegPageLocators.NEXT)
        next_button.click()

    def get_error_number_text(self):
        number_error = self.findelement(RegPageLocators.ERROR_NUMBER_PHONE)
        return number_error.text


