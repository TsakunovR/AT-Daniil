from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class RecoveryPageLocators2:
    POST = (By.XPATH,'//*[@class="ext-registration_stubs"]//*[@data-l="t,email"]')
    GET_CODE_ON_POST = (By.XPATH,'//*[@class="form-actions mt-5x"]//*[@data-l="t,submit"]')
    WRONG_POST =(By.XPATH,'//*[@class="input-e"]')


class RecoveryPageHelper2(BasePage):
    def __check_page(self):
        self.findElement(RecoveryPageLocators2.POST)
        self.findElement(RecoveryPageLocators2.GET_CODE_ON_POST)
        self.findElement(RecoveryPageLocators2.WRONG_POST)


    def click_on_post(self):
        on_post = self.findElement(RecoveryPageLocators2.POST)
        on_post.click()


    def get_code_post(self):
        send_on_post = self.findElement(RecoveryPageLocators2.GET_CODE_ON_POST)
        send_on_post.click()


    def get_text_wrong_post(self):
        info_wrong_post = self.findElement(RecoveryPageLocators2.WRONG_POST)
        return info_wrong_post.text

