from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class RegPageLocators:
    REGISTRATION = (By.XPATH,'//*[@data-l="t,register"]')
    NUMBER_FIELD = (By.XPATH,'//*[@id="field_phone"]')
    ERROR_NUMBER_PHONE = (By.XPATH,'//*[@class="input-e js-ph-vl-hint"]')
    NEXT = (By.XPATH,'//*[@data-l="t,submit"]')
    COUNTRY_LIST = (By.XPATH,'//div[@data-l="t,country"]')
    COUNTRY_ELEMENT = (By.XPATH,'//*[@class="country-select_i"]')
    COUNTRY_CODE = (By.XPATH,'//*[@data-id="10423319006"]')
    HELP_BUTTON = (By.XPATH,'//*[@class="anon-tb-item"]')




class RegPageHelper(BasePage):
    def __check_page(self):
            self.findelement(RegPageLocators.REGISTRATION)
            self.findelement(RegPageLocators.ERROR_NUMBER_PHONE)
            self.findelement(RegPageLocators.NUMBER_FIELD)
            self.findelement(RegPageLocators.NEXT)
            self.findelement(RegPageLocators.COUNTRY_LIST)
            self.findelement(RegPageLocators.COUNTRY_ELEMENT)
            self.findelement(RegPageLocators.COUNTRY_CODE)
            self.findelement(RegPageLocators.HELP_BUTTON)



    def click_reg_button(self):
        reg_button = self.findelement(RegPageLocators.REGISTRATION)
        reg_button.click()


    def click_next_button(self):
        next_button = self.findelement(RegPageLocators.NEXT)
        next_button.click()

    def get_error_number_text(self):
        number_error = self.findelement(RegPageLocators.ERROR_NUMBER_PHONE)
        return number_error.text

    def select_country(self,index):
        country_list = self.findelement(RegPageLocators.COUNTRY_LIST)
        country_list.click()
        country_element = self.findelements(RegPageLocators.COUNTRY_ELEMENT)
        country_element[index].click()

    def get_country_code(self):
        country_code_element = self.findelement(RegPageLocators.COUNTRY_CODE)
        displayed_code = country_code_element.get_attribute("value")
        return displayed_code


    def click_help_button(self):
        sos_button = self.findelement(RegPageLocators.HELP_BUTTON)
        sos_button.click()










