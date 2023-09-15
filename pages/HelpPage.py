from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class HelpPageLocators:
    TITLE = (By.XPATH,'//*[@class="title__7mcdl"]')


class HelpPageHelper(BasePage):
    def __check_page(self):
        self.findelement(HelpPageLocators.TITLE)


    def get_help_title(self):
        title_help = self.findelement(HelpPageLocators.TITLE)
        return title_help.text

