class BasePage():
    """
    The base page from which all other classes will be inherited. Here we
    will describe auxiliary methods for working with the driver
    """
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        """
        The method will open the desired page in the browser
        """
        self.browser.get(self.url)
