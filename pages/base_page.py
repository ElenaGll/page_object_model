from selenium.common.exceptions import NoSuchElementException


class BasePage:
    """
    The base page from which all other classes will be inherited. Here we
    will describe auxiliary methods for working with the driver
    """
    def __init__(self, browser, url, timeout=4):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """
        The method will open the desired page in the browser
        """
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

