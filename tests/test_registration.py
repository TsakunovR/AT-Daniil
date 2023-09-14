from BaseTest import browser
from pages.BasePage import BasePage
from pages.RegPage import RegPageHelper
from pages.LoginPage import LoginPageHelper
import allure


@allure.suite('Проверка кнопки регистрации ')
class TestRegNot:
    def test_empty_reg_form(self, browser):
        base_page = BasePage(browser)
        with allure.step('Открываем страницу авторизации'):
            base_page.go_to_url("https://ok.ru")
            login_page = LoginPageHelper(browser)
        with allure.step('Кликаем Зарегистрироваться'):
            login_page.click_reg_button()
        with allure.step('Кликаем Далее'):
            reg_page = RegPageHelper(browser)
            reg_page.click_next_button()
        with allure.step('Проверяем отображение ошибки'):
            allure.attach(
                browser.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        assert reg_page.get_error_number_text() == 'Неправильный номер телефона.'


    def test_country_button(self, browser):
        base_page = BasePage(browser)
        with allure.step('Открываем страницу авторизации'):
            base_page.go_to_url("https://ok.ru")
            login_page = LoginPageHelper(browser)
        with allure.step('Кликаем Зарегистрироваться'):
            login_page.click_reg_button()
        with allure.step('Кликаем на кнопку выбора страны и выбираем Беларусь'):
            reg_page = RegPageHelper(browser)
            reg_page.select_country(0)
        with allure.step('Проверяем отображение кода страны'):
            allure.attach(
                browser.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
            assert reg_page.get_country_code() == '+375'














