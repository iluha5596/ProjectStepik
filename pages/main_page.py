import time
from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage


class MainPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        alert = self.browser.switch_to.alert
        alert.accept()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def search_book(self):
        search_bar_link = self.browser.find_element(*MainPageLocators.SEARCH_BAR)
        search_bar_link.send_keys(self.name_book)
        find_link = self.browser.find_element(*MainPageLocators.FIND)
        find_link.click()
        img_book_link = self.browser.find_element(*MainPageLocators.IMG_BOOK)
        img_book_link.click()


