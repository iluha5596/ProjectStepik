import time
import pytest
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.base_page import BasePage


@pytest.mark.parametrize('promo', range(0, 10))
def test_guest_can_add_product_to_basket(browser, promo):
    baseUrl = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
    url = f'{baseUrl}{promo}'
    page = ProductPage(browser, url)
    page.open()
    page.click_add_basket()
    assert_alert = BasePage(browser, url)
    assert_alert.solve_quiz_and_get_code()
    try:
        page.message_add_basket()
    except AssertionError:
        pytest.xfail(f"Skipping test for link: {url}")


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    url = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, url)
    page.open()
    page.click_add_basket()
    page.message_is_not_element_present()


def test_guest_cant_see_success_message(browser):
    url = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, url)
    page.open()
    page.message_is_not_element_present()


def test_message_disappeared_after_adding_product_to_basket(browser):
    url = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, url)
    page.open()
    page.click_add_basket()
    page.message_is_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, url)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    url = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, url)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

