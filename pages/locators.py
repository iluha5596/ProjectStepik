from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_VIEW_BASKET = (By.XPATH, '//a[@class="btn btn-default"]')
    USER_ICON = (By.XPATH, '//i[@class="icon-user"]')


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    SEARCH_BAR = (By.XPATH, '//input[@type="search"]')
    FIND = (By.XPATH, '//input[@type="submit"]')
    IMG_BOOK = (By.XPATH, '//h3/a')


class LoginPageLocators:
    LOGIN_EMAIL = (By.XPATH, '//input[@name="login-username"]')
    LOGIN_PASS = (By.XPATH, '//input[@name="login-password"]')
    BUTTON_LOGIN = (By.XPATH, '//button[@name="login_submit"]')
    REGISTRATION_EMAIL = (By.XPATH, '//input[@name="registration-email"]')
    REGISTRATION_PASS_FIRST = (By.XPATH, '//input[@name="registration-password1"]')
    REGISTRATION_PASS_SECOND = (By.XPATH, '//input[@name="registration-password2"]')
    BUTTON_REGISTRATION = (By.XPATH, '//button[@name="registration_submit"]')


class ProductPageLocators:
    BUTTON_ADD_BASKET = (By.XPATH, '//form[@id="add_to_basket_form"]/button[@type="submit"]')
    NAME_BOOK = (By.XPATH, '//div/h1')
    PRICE_BOOK = (By.XPATH, '(//p[@class="price_color"])[1]')
    MESSAGE_NAME_BOOK = (By.XPATH, '(//div[@class="alertinner "]/strong)[1]')
    MESSAGE_PRICE_BOOK = (By.XPATH, '(//div[@class="alertinner "])/p/strong')
    MESSAGE_ADD_BOOK = (By.XPATH, '//div[@class="alert alert-safe alert-noicon alert-success  fade in"]/div['
                                  '@class="alertinner "]')


class BasketPageLocators:
    PRODUCT_ELEMENT = (By.XPATH, '//form[@class="basket_summary"]')
    BASKET_EMPTY = (By.XPATH, '//div[@id="content_inner"]/p')
