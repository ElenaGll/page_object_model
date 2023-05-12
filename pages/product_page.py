from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()
        self.solve_quiz_and_get_code()

    def book_should_be_added(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_IS_ADDED), \
            'Book has not been added'

    def price_should_be_right(self):
        price_of_book_el = self.browser.find_element(*ProductPageLocators.PRICE_OF_BOOK)
        price_of_book = price_of_book_el.text
        price_of_book_in_basket_el = self.browser.find_element(*ProductPageLocators.PRICE_OF_BOOK_IN_BASKET)
        price_of_book_in_basket_all = price_of_book_in_basket_el.text
        length_price = len(price_of_book)
        price_of_book_in_basket = price_of_book_in_basket_all[-length_price::]
        assert price_of_book == price_of_book_in_basket, \
            'Prices are not equal'
