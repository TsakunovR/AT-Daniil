from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
        LOGIN_FIELD = (By.XPATH, '//*[@id="field_email"]')
        PASSWORD_FILED = (By.XPATH, '//*[@type="password"]')
        LOGIN_BUTTON = (By.XPATH, './/*[@data-l="t,sign_in"]')
        IN_QR = (By.XPATH,'//*[@data-l="t,get_qr"]')
        LOGIN_FOGOT = (By.XPATH,'//*[@data-l="t,restore"]')
        REGISTRATION = (By.XPATH,'//*[@class="login-form-actions"]//*[@data-l="t,register"]')
        ICON_VK = (By.XPATH,'//*[@data-l="t,vkc"]')
        ICON_MAIL = (By.XPATH,'//*[@data-l="t,mailru"]')
        ICON_GO = (By.XPATH,'//*[@data-l="t,google"]')
        ICON_YA = (By.XPATH,'//*[@data-l="t,yandex"]')
        ICON_APPLE = (By.XPATH,'//*[@data-l="t,apple"]')
        ERROR_FIELD = (By.XPATH, '//*[@class="input-e login_error"]')
        INFO_TEXT = (By.XPATH,'//*[@class="qr_code_info_header"]')
        GIFTS_BUTTON = (By.XPATH,'//*[@href="https://ok.ru/gifts"]')


class LoginPageHelper(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__check_page()

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
            self.findElement(LoginPageLocators.GIFTS_BUTTON)
    def click_login_button(self):
        login_button = self.findElement(LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

    def get_error_text(self):
        error_field = self.findElement(LoginPageLocators.ERROR_FIELD)
        return error_field.text

    def login_send_keys(self,text):
        loginkeys = self.findElement(LoginPageLocators.LOGIN_FIELD)
        loginkeys.send_keys(text)

    def click_reg_button(self):
        reg_button = self.findElement(LoginPageLocators.REGISTRATION)
        reg_button.click()

    def click_qr_button(self):
        qr_button = self.findElement(LoginPageLocators.IN_QR)
        qr_button.click()


    def get_info_text(self):
        info_text = self.findElement(LoginPageLocators.INFO_TEXT)
        return info_text.text


    def click_gifts_button(self):
        gifts_button = self.findElement(LoginPageLocators.GIFTS_BUTTON)
        gifts_button.click()


