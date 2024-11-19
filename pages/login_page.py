from data.test_data import Page
from data.helper import Locators

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = Locators.username_field
        self.password_field = Locators.password_field
        self.login_button = Locators.login_button

    # Redirect to the page
    def load(self):
        self.driver.get(Page.url)

    # User login
    def login(self, username, password):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    # If user login with invalid data
    def error_login(self):
        return self.driver.find_element(*Locators.error_login_message).text