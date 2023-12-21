from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_by_add_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_BASKET), 'No such button add basket'

    def click_add_basket(self):
        button_add_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_BASKET)
        button_add_basket.click()

    def message_add_basket(self):
        message_name_book_link = self.browser.find_element(*ProductPageLocators.MESSAGE_NAME_BOOK)
        message_price_book_link = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE_BOOK)
        name_book_link = self.browser.find_element(*ProductPageLocators.NAME_BOOK)
        price_book_link = self.browser.find_element(*ProductPageLocators.PRICE_BOOK)
        name_book = name_book_link.text
        price_book = price_book_link.text
        message_name_book = message_name_book_link.text
        message_price_book = message_price_book_link.text
        assert name_book in message_name_book, 'Incorrect book title in the message when adding to basket'
        assert price_book in message_price_book, 'Incorrect book price in the message when adding to basket'

