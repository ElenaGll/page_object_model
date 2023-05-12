from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import pytest

link1 = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
link2 = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
link3 = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'


@pytest.mark.parametrize('number', ['0', '1', '2', '3', '4', '5', '6',
                                    pytest.param('7', marks=pytest.mark.xfail),
                                    '8', 9])
def test_guest_can_add_product_to_basket(browser, number):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.book_should_be_added()
    page.price_should_be_right()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link1)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link1)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link1)
    page.open()
    page.add_product_to_basket()
    page.message_should_be_dissapeared()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link3)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link3)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
