from selenium.webdriver.common.by import By


class BasicPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, 'div.row div.basket-mini span.btn-group a.btn-default')
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class BasketPageLocators():
    TEXT_ABOUT_EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner p')
    BASKET_TITLE = (By.CSS_SELECTOR, '#content_inner div.basket-title div.row h2')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, 'div.login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, 'div.register_form')
    REGISTER_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_PASSWORD_CONFIRM = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_SUBMIT = (By.NAME, 'registration_submit')


class MainPageLocators():
    MAIN_LINK = (By.CSS_SELECTOR, 'div.page_inner ul.breadcrumb li:first-of-type')


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    NAME_OF_BOOK = (By.CSS_SELECTOR, 'div.content div.product_main h1')
    NAME_OF_BOOK_IN_BASKET = (By.CSS_SELECTOR, '#messages div.alert-success div.alertinner strong')
    PRICE_OF_BOOK = (By.CSS_SELECTOR, 'div.content div.product_main p.price_color')
    PRICE_OF_BOOK_IN_BASKET = (By.CSS_SELECTOR, '#messages div.alert-info div.alertinner p strong')
