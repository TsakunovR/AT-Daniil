from BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper

class TestNotAuth:
    def test_empty_auth_form(self, browser):
        base_page = BasePage(browser)
        base_page.go_to_url("https://ok.ru")
        login_page = LoginPageHelper(browser)
        login_page.click_login_button()
        assert login_page.get_error_text() == "Введите логин"


    def test_login_field(self, browser):
        base_page = BasePage(browser)
        base_page.go_to_url("https://ok.ru")
        login_page = LoginPageHelper(browser)
        login_page.login_send_keys('qwerty')
        login_page = LoginPageHelper(browser)
        login_page.click_login_button()
        assert login_page.get_error_text() == "Введите логин"
