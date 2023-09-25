from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class RecoveryPageLocators1:
    NUMBER = (By.XPATH,'//*[@class="ext-registration_stubs"]//*[@data-l="t,phone"]')
    GET_CODE_ON_PHONE = (By.XPATH,'//*[@class="form-actions mt-5x"]//*[@data-l="t,submit"]')
    WRONG_PHONE =(By.XPATH,'//*[@class="input-e js-ph-vl-hint"]')



class RecoveryPageHelper1(BasePage):

    def __check_page(self):
        self.findElement(RecoveryPageLocators1.NUMBER)
        self.findElement(RecoveryPageLocators1.GET_CODE_ON_PHONE)
        self.findElement(RecoveryPageLocators1.WRONG_PHONE)

    def click_on_phone(self):
        on_phone = self.findElement(RecoveryPageLocators1.NUMBER)
        on_phone.click()


    def get_code_phone(self):
        on_phone = self.findElement(RecoveryPageLocators1.GET_CODE_ON_PHONE)
        on_phone.click()


    def get_text_wrong_phone(self):
        info_wrong_phone = self.findElement(RecoveryPageLocators1.WRONG_PHONE)
        return info_wrong_phone.text





