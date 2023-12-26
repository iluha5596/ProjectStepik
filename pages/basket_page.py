from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def check_basket_page(self):
        self.check_no_items_in_basket()
        self.check_message_your_cart_empty()

    def check_no_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_ELEMENT), 'Products should not be displayed in ' \
                                                                                 'an empty basket '

    def check_message_your_cart_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), 'No messages "Your basket is empty"'
