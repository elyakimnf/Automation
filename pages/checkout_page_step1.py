from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.postal_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.cancel_button = (By.ID, "cancel")
        # complete checkout page
        self.finish_button = (By.ID, "finish")
        self.success_message = (By.CLASS_NAME, "complete-header")

    # user input checkout information
    def checkout_info(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.first_name_field).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        self.driver.find_element(*self.postal_code_field).send_keys(postal_code)

    # user continue checkout
    def continue_checkout(self):
        self.driver.find_element(*self.continue_button).click()

    # user cancel checkout
    def cancel_checkout(self):
        self.driver.find_element(*self.cancel_button).click()

    # user finish checkout
    def finish_checkout(self):
        self.driver.find_element(*self.finish_button).click()

    # user success checkout
    def get_success_message(self):
        return self.driver.find_element(*self.success_message).text
