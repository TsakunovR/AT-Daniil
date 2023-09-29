from pages.BasePage import BasePage
from selenium.webdriver.common.by import By



class GetCodeOnPhoneLocators:
    GET_CODE_ON_PHONE = (By.XPATH,'//*[@class="form-actions mt-5x"]//*[@data-l="t,submit"]')
    WRONG_PHONE = (By.XPATH, '//*[@class="input-e js-ph-vl-hint"]')
    PHONE_FIElD = (By.XPATH,'//*[@data-l="t,phone"]')
    COUNTRY_FIELD = (By.XPATH,'//*[@data-locale="ru"]')

class GetCodeOnPhonePageHelper(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__check_page()


    def __check_page(self):
        self.findElement(GetCodeOnPhoneLocators.GET_CODE_ON_PHONE)
        self.findElement(GetCodeOnPhoneLocators.WRONG_PHONE)
        self.findElement(GetCodeOnPhoneLocators.PHONE_FIElD)
        self.findElement(GetCodeOnPhoneLocators.COUNTRY_FIELD)


    def get_code_phone(self):
        on_phone = self.findElement(GetCodeOnPhoneLocators.GET_CODE_ON_PHONE)
        on_phone.click()


    def get_text_wrong_phone(self):
        info_wrong_phone = self.findElement(GetCodeOnPhoneLocators.WRONG_PHONE)
        return info_wrong_phone.text