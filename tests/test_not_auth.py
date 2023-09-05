from BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
import allure
@allure.suite ('Проверка валидации пустой формы авторизации')
class TestNotAuth:
    def test_empty_auth_form(self, browser):
        base_page = BasePage(browser)
        with allure.step ('Открываем страницу авторизации'):
            base_page.go_to_url("https://ok.ru")
            login_page = LoginPageHelper(browser)
        with allure.step('Кликаем войти'):
            login_page.click_login_button()
        with allure.step('Проверяем отображение ошибки'):
            allure.attach(
                browser.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        assert login_page.get_error_text() == "Введите логин"

    @allure.suite('Проверка валидации с пустым паролем ')
    def test_login_field(self, browser):
        base_page = BasePage(browser)
        with allure.step('Открываем страницу авторизации'):
            base_page.go_to_url("https://ok.ru")
            login_page = LoginPageHelper(browser)
        with allure.step('Пишем в поле логин - qwerty'):
            login_page.login_send_keys('qwerty')
        with allure.step('Кликаем войти'):
            login_page.click_login_button()
        with allure.step('Проверяем отображение ошибки'):
            allure.attach(
                browser.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
                )
        assert login_page.get_error_text() == "Введите пароль"
