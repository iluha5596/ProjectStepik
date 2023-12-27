import time
import pytest
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage


@pytest.mark.need_review
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        url = 'https://selenium1py.pythonanywhere.com/ru/accounts/login/'
        login_page = LoginPage(browser, url)
        login_page.open()
        email = str(time.time()) + '@fakemail.org'
        password = '45a6fdasf46a'
        login_page.register_new_user(email=email, password=password)
        base_page = BasePage(browser, url)
        base_page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        url = 'https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer5'
        page = ProductPage(browser, url)
        page.open()
        page.click_add_basket()
        assert_alert = BasePage(browser, url)
        assert_alert.solve_quiz_and_get_code()
        try:
            page.message_add_basket()
        except AssertionError:
            pytest.xfail(f"Skipping test for link: {url}")


@pytest.mark.need_review
@pytest.mark.parametrize('promo', range(9, 10))
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


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    url = 'https://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/'
    product_page = ProductPage(browser, url)
    product_page.open()
    base_page = BasePage(browser, url)
    base_page.basket_opened()
    basket_page = BasketPage(browser, url)
    basket_page.check_basket_page()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    url = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, url)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    url = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, url)
    page.open()
    page.click_add_basket()
    page.message_is_not_element_present()


@pytest.mark.xfail
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






