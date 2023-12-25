import time
import pytest
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.base_page import BasePage


def test_guest_shold_see_login_link_main_page(browser):
    url = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, url)
    page.open()
    page.should_by_login_link()


def test_guest_can_go_to_login_page_main_page(browser):
    url = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, url)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_my_test(browser):
    url = 'http://selenium1py.pythonanywhere.com/'
    name_book = "The shellcoder's handbook"
    page = MainPage(browser, url, name_book)
    page.open()
    page.search_book()



