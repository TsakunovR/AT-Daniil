from pages.BasePage import BasePage
from pages.RegPage import RegPageHelper
from pages.LoginPage import LoginPageHelper
from pages.HelpPage import HelpPageHelper
from pages.GiftsPage import GiftsPageHelper
import allure
from BaseTest import browser


@allure.suite('Проверка страницы подарков')
class TestGiftsPage:
    def test_gifts_button(self, browser):
        with allure.step('Открываем страницу авторизации'):
            base_page = BasePage(browser)
            base_page.go_to_url("https://ok.ru")
        with allure.step('Кликаем на подарки'):
            gifts_page = LoginPageHelper(browser)
            gifts_page.click_gifts_button()
        with allure.step('Скролим до кнопки '):
            more_show_button = GiftsPageHelper(browser)
            more_show_button.scrollToshowMoreButton()
        with allure.step('Кликаем на кнопку показать больше'):
            click_more = GiftsPageHelper(browser)
            click_more.click_more_button()
        with allure.step('Проверяем отображение леера '):
            click_sign = GiftsPageHelper(browser)
            click_sign.click_sign_in()
            allure.attach(
                browser.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )








