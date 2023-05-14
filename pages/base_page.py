from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from .locators import BasicPageLocators
import math


class BasePage:
    """
    The base page from which all other classes will be inherited. Here we
    will describe auxiliary methods for working with the driver
    """
    def __init__(self, browser, url, timeout=4):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_basket_page(self):
        basket_link = self.browser.find_element(*BasicPageLocators.BASKET_LINK)
        basket_link.click()

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasicPageLocators.LOGIN_LINK)
        login_link.click()

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(expected_conditions.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(expected_conditions.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def open(self):
        """
        The method will open the desired page in the browser
        """
        self.browser.get(self.url)

    def should_be_login_link(self):
        assert self.is_element_present(*BasicPageLocators.LOGIN_LINK), \
            'Login link is not presented'

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except (NoAlertPresentException, TimeoutException):
            print("No second alert presented")
