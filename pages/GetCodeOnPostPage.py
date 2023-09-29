from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class GetCodeOnPostPageLocators:
    GET_CODE_ON_POST = (By.XPATH, '//*[@data-l="t,submit"]')
    WRONG_POST = (By.XPATH, '//div[@class="input-e"]')
    EMAIL_FIELD = (By.XPATH, '//*[@data-l="t,email"]')



class GetCodeOnPostHelper(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__check_page()


    def __check_page(self):
        self.findElement(GetCodeOnPostPageLocators.GET_CODE_ON_POST)
        self.findElement(GetCodeOnPostPageLocators.EMAIL_FIELD)


    def get_code_post(self):
        send_on_post = self.findElement(GetCodeOnPostPageLocators.GET_CODE_ON_POST)
        send_on_post.click()

    def get_text_wrong_post(self):
        info_wrong_post = self.findElement(GetCodeOnPostPageLocators.WRONG_POST)
        return info_wrong_post.text
