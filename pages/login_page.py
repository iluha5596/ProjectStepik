from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(LoginPage, self).__init__(*args, **kwargs)

    def register_new_user(self, email, password):
        input_email_reg = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        input_pass_ref_first = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASS_FIRST)
        input_pass_ref_second = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASS_SECOND)
        button_reg = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION)
        input_email_reg.send_keys(email)
        input_pass_ref_first.send_keys(password)
        input_pass_ref_second.send_keys(password)
        button_reg.click()

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
