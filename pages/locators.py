from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_EMAIL = (By.XPATH, '//input[@name="login-username"]')
    LOGIN_PASS = (By.XPATH, '//input[@name="login-password"]')
    BUTTON_LOGIN = (By.XPATH, '//button[@name="login_submit"]')
    REGISTRATION_EMAIL = (By.XPATH, '//input[@name="registration-email"]')
    REGISTRATION_PASS_FIRST = (By.XPATH, '//input[@name="registration-password1"]')
    REGISTRATION_PASS_SECOND = (By.XPATH, '//input[@name="registration-password2"]')
    BUTTON_REGISTRATION = (By.XPATH, '//button[@name="registration_submit"]')
