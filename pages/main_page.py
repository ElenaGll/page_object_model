from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    """
    The method is linked to the main page of the online store
    """

    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, '#login_link')
        login_link.click()
