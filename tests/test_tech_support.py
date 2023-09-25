from pages.BasePage import BasePage
from pages.RegPage import RegPageHelper
from pages.LoginPage import LoginPageHelper
from pages.HelpPage import HelpPageHelper
from pages.GiftsPage import GiftsPageHelper
from pages.RecoveryPage1 import RecoveryPageHelper1
from pages.RecoveryPage2 import RecoveryPageHelper2
from pages.RecoveryPage3 import RecoveryPageHelper3
import allure
from BaseTest import browser


@allure.suite('Проверка отображения окна поддержки ')
class TestSupport:
    def test_win_sup(self, browser):
        with allure.step('Открываем страницу авторизации'):
            base_page = BasePage(browser)
            base_page.go_to_url("https://ok.ru")
        with allure.step('Кликаем не получается войти'):
            login_page = LoginPageHelper(browser)
            login_page.click_no_entry()
        with allure.step('Кликаем обратиться в поддержку'):
            rec_page = RecoveryPageHelper3(browser)
            rec_page.click_on_support()
        with allure.step('Проверяем окно поддержки кликаем на кнопку закрытия окна'):
            rec_page.click_win_sup()
            allure.attach(
                browser.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
            rec_page.click_win_sup()
