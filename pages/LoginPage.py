from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
        LOGIN_FIELD = (By.XPATH, '//*[@id="field_email"]')
        PASSWORD_FILED = (By.XPATH, '//*[@type="password"]')
        LOGIN_BUTTON = (By.XPATH, './/*[@data-l="t,sign_in"]')
        IN_QR = '//*[@data-l="t,get_qr"]'
        LOGIN_FOGOT = '//*[@data-l="t,restore"]'
        REGISTRATION = '//*[@data-l="t,register"]'
        ICON_VK = '//*[@data-l="t,vkc"]'
        ICON_MAIL = '//*[@data-l="t,mailru"]'
        ICON_GO = '//*[@data-l="t,google"]'
        ICON_YA = '//*[@data-l="t,yandex"]'
        ICON_APPLE = '//*[@data-l="t,apple"]'
        ERROR_FIELD = (By.XPATH, '//*[@class="input-e login_error"]')


class LoginPageHelper(BasePage):
    def __check_page(self):
            self.findElement(LoginPageLocators.LOGIN_FIELD)
            self.findElement(LoginPageLocators.PASSWORD_FILED)
            self.findElement(LoginPageLocators.LOGIN_BUTTON)
            self.findElement(LoginPageLocators.IN_QR)
            self.findElement(LoginPageLocators.LOGIN_FOGOT)
            self.findElement(LoginPageLocators.REGISTRATION)
            self.findElement(LoginPageLocators.ICON_VK)
            self.findElement(LoginPageLocators.ICON_MAIL)
            self.findElement(LoginPageLocators.ICON_GO)
    def click_login_button(self):
        login_button = self.findelement(LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

    def get_error_text(self):
        error_field = self.findelement(LoginPageLocators.ERROR_FIELD)
        return error_field.text
    def login_send_keys(self,text):
        loginkeys = self.findelement(LoginPageLocators.LOGIN_FIELD)
        loginkeys.send_keys(text)
