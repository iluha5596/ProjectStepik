from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'Substring "login" is not present in the current URL'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL) and \
               self.is_element_present(*LoginPageLocators.LOGIN_PASS) and \
               self.is_element_present(*LoginPageLocators.BUTTON_LOGIN), 'No login form'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL) and \
               self.is_element_present(*LoginPageLocators.REGISTRATION_PASS_FIRST) and \
               self.is_element_present(*LoginPageLocators.REGISTRATION_PASS_SECOND) and \
               self.is_element_present(*LoginPageLocators.BUTTON_REGISTRATION), 'No registration form'
