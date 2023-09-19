from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class GiftsPageLocators:
    MORE_BUTTON = (By.XPATH,'//*[@class="gifts-catalog-categories_button"]')
    CLICK_BUTTON = (By.XPATH,'//*[@class="button-pro __sec h-mod"]')
    SIGN_IN = (By.XPATH,'//*[@data-l="t,sign_in"]')


class GiftsPageHelper(BasePage):
        def scrollToshowMoreButton(self):
            self.driver.execute_script('arguments[0].scrollIntoView(true)',self.findElement(GiftsPageLocators.MORE_BUTTON))

        def click_more_button(self):
            show_button = self.findElement(GiftsPageLocators.CLICK_BUTTON)
            show_button.click()

        def __init__(self, driver):
            super().__init__(driver)
            self.__check_page()

        def __check_page(self):
            self.findElement(GiftsPageLocators.MORE_BUTTON)
            self.findElement(GiftsPageLocators.CLICK_BUTTON)


        def click_sign_in(self):
            sign_in = self.findElement(GiftsPageLocators.SIGN_IN)
            sign_in.click()


