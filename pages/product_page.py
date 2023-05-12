from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()
        self.solve_quiz_and_get_code()

    def book_should_be_added(self):
        name_of_book_el = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK)
        name_of_book = name_of_book_el.text
        name_of_book_in_basket_el = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK_IN_BASKET)
        name_of_book_in_basket = name_of_book_in_basket_el.text
        assert name_of_book == name_of_book_in_basket, \
            'Book has not been added'

    def price_should_be_right(self):
        price_of_book_el = self.browser.find_element(*ProductPageLocators.PRICE_OF_BOOK)
        price_of_book = price_of_book_el.text
        price_of_book_in_basket_el = self.browser.find_element(*ProductPageLocators.PRICE_OF_BOOK_IN_BASKET)
        price_of_book_in_basket = price_of_book_in_basket_el.text
        assert price_of_book == price_of_book_in_basket, \
            'Prices are not equal'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.NAME_OF_BOOK_IN_BASKET), \
            'Success message is presented, but should not be'

    def message_should_be_dissapeared(self):
        assert self.is_disappeared(*ProductPageLocators.NAME_OF_BOOK_IN_BASKET), \
            'Success message is presented, but should not be'
