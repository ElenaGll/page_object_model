from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    """
    The method is linked to the main page of the online store
    """

    def go_to_main_page(self):
        main_link = self.browser.find_element(*MainPageLocators.MAIN_LINK)
        main_link.click()
