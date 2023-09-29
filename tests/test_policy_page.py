from pages.BasePage import BasePage
from pages.RegPage import RegPageHelper
from pages.LoginPage import LoginPageHelper
from pages.HelpPage import HelpPageHelper
from pages.GiftsPage import GiftsPageHelper
from pages.RecoveryPage1 import RecoveryPageHelper1
from pages.SupportPage import SupportPageHelper
from pages.PolicyPage import PolicyPageHelper
import allure
from BaseTest import browser


@allure.suite('Проверка отображения соглашения и политики ')
class TestАgreementPolicy:
    def test_policy(self, browser):
        with allure.step('Открываем страницу авторизации'):
            base_page = BasePage(browser)
            base_page.go_to_url("https://ok.ru")
        with allure.step('Кликаем еще затем кликаем политики'):
            login_page = LoginPageHelper(browser)
            login_page.hover_and_click_on_more()
        with allure.step('Проверяем страницу соглашения и политики'):
            policy_page = PolicyPageHelper(browser)
            allure.attach(
                browser.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )

