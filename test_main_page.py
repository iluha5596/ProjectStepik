from .pages.login_page import LoginPage
from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    url = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, url)
    page.open()
    page.go_to_login_page()


def test_guest_shold_see_login_link(browser):
    url = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, url)
    page.open()
    page.should_by_login_link()


def test_guest_can_go_to_login_page(browser):
    url = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, url)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
