from selenium.webdriver.common.by import By
from data.test_data import Page

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    # Redirect to the page
    def load(self):
        self.driver.get(Page.url)

    # user login
    def login(self, username, password):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()
    #
    # # Redirect to the page
    # def load(self, url):
    #     self.driver.get(url)
    #
    # # user input username
    # def enter_username(self, username):
    #     self.driver.find_element(*self.username_field).clear()
    #     self.driver.find_element(*self.username_field).send_keys(username)
    #
    # # user input password
    # def enter_password(self, password):
    #     self.driver.find_element(*self.password_field).clear()
    #     self.driver.find_element(*self.password_field).send_keys(password)
    #
    # # user click login button
    # def click_login(self):
    #     self.driver.find_element(*self.login_button).click()
    #
    # #  complete login
    # def user_login(self, username, password):
    #     self.enter_username(username)
    #     self.enter_password(password)
    #     self.click_login()
