from pages.BasePage import BasePage
from pages.RegPage import RegPageHelper
from pages.LoginPage import LoginPageHelper
from pages.HelpPage import HelpPageHelper
from pages.GiftsPage import GiftsPageHelper
from pages.RecoveryPage1 import RecoveryPageHelper1
from pages.RecoveryPage2 import RecoveryPageHelper2
import allure
from BaseTest import browser


@allure.suite('Проверка восстановления пароля с помощью телефона  ')
class TestNotEnter:
    def test_not_enter(self, browser):
        with allure.step('Открываем страницу авторизации'):
            base_page = BasePage(browser)
            base_page.go_to_url("https://ok.ru")
        with allure.step('Кликаем не получается войти'):
            login_page = LoginPageHelper(browser)
            login_page.click_no_entry()
        with allure.step('Кликаем на значок телефона'):
            rec_page = RecoveryPageHelper1(browser)
            rec_page.click_on_phone()
        with allure.step('Кликаем получить код '):
            rec_page.get_code_phone()
        with allure.step('Проверяем отображение ошибки'):
            allure.attach(
                browser.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        assert rec_page.get_text_wrong_phone() == 'Неправильный номер телефона.'

    @allure.suite('Проверка восстановления пароля с помощью почты  ')
    def test_not_enter2(self, browser):
        with allure.step('Открываем страницу авторизации'):
            base_page = BasePage(browser)
            base_page.go_to_url("https://ok.ru")
        with allure.step('Кликаем не получается войти'):
            login_page = LoginPageHelper(browser)
            login_page.click_no_entry()
        with allure.step('Кликаем на значок телефона'):
            rec_page = RecoveryPageHelper2(browser)
            rec_page.click_on_post()
        with allure.step('Кликаем получить код '):
            rec_page.get_code_post()
        with allure.step('Проверяем отображение ошибки'):
            allure.attach(
                browser.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        assert rec_page.get_text_wrong_post() == 'Неправильный формат почты'



