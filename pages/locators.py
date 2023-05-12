from selenium.webdriver.common.by import By


class MainPageLocaators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, 'div.login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, 'div.register_form')

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    BOOK_IS_ADDED = (By.CSS_SELECTOR, '#messages div.alert-success')
    PRICE_OF_BOOK = (By.CSS_SELECTOR, 'div.content div.product_main p.price_color')
    PRICE_OF_BOOK_IN_BASKET = (By.CSS_SELECTOR, '#messages div.alert-info div.alertinner p')
