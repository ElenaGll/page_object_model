from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TITLE), \
            'Basket does not empty'

    def should_be_text_about_empty_basket(self):
        text_empty_basket_el = self.browser.find_element(*BasketPageLocators.TEXT_ABOUT_EMPTY_BASKET)
        text_empty_basket = text_empty_basket_el.text
        assert 'Your basket is empty. Continue shopping' == text_empty_basket, \
            'Text about empty basket is not presented'

    def text_about_empty_basket_should_be_dissapeared(self):
        assert self.is_disappeared(*BasketPageLocators.TEXT_ABOUT_EMPTY_BASKET), \
            'Text about empty basket is presented, but should not be'
