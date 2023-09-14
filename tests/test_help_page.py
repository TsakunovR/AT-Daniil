from pages.BasePage import BasePage
from pages.RegPage import RegPageHelper
from pages.LoginPage import LoginPageHelper
from pages.HelpPage import HelpPageHelper
import allure
from BaseTest import browser


@allure.suite('Проверка страницы помощи')
class TestHelpPage:
    def test_help_title(self, browser):
        base_page = BasePage(browser)
        with allure.step('Открываем страницу авторизации'):
            base_page.go_to_url("https://ok.ru")
            login_page = LoginPageHelper(browser)
        with allure.step('Кликаем Зарегистрироваться'):
            login_page.click_reg_button()
        with allure.step('Кликаем на кнопку помощь'):
            reg_page = RegPageHelper(browser)
            reg_page.click_help_button()
        with allure.step('Проверяем отображение заголовка'):
            help_page = HelpPageHelper(browser)
            allure.attach(
                browser.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        assert help_page.get_help_title() == 'Чем мы можем вам помочь?'
