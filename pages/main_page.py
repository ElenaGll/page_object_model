from .base_page import BasePage


class MainPage(BasePage):
    """
    The method is linked to the main page of the online store
    """

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
