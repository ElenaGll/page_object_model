from .pages.login_page import LoginPage

link = 'http://selenium1py.pythonanywhere.com/'


def test_should_be_login_page(browser):
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_page()
