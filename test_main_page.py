import time
import pytest
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage


def test_guest_shold_see_login_link_main_page(browser):
    url = 'http://selenium1py.pythonanywhere.com/'
    page = BasePage(browser, url)
    page.open()
    page.should_be_login_link()


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


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    url = 'http://selenium1py.pythonanywhere.com/'
    base_page = BasePage(browser, url)
    base_page.open()
    base_page.basket_opened()
    basket_page = BasketPage(browser, url)
    basket_page.check_basket_page()
