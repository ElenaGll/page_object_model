from .base_page import BasePage
from .locators import MainPageLocaators


class MainPage(BasePage):
    """
    The method is linked to the main page of the online store
    """

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocaators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocaators.LOGIN_LINK), \
            'Login link is not presented'
