import pytest

from .pages.login_page import LoginPage
from .pages.main_page import MainPage

link = 'http://selenium1py.pythonanywhere.com/'


@pytest.fixture
def login_url(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    return browser.current_url


def test_should_be_login_url(browser, login_url):
    page = LoginPage(browser, login_url)
    page.open()
    page.should_be_login_url()


def test_should_be_login_form(browser, login_url):
    page = LoginPage(browser, login_url)
    page.open()
    page.should_be_login_form()


def test_should_be_register_form(browser, login_url):
    page = LoginPage(browser, login_url)
    page.open()
    page.should_be_register_form()
