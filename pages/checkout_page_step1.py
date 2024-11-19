from data.helper import Locators


class CheckoutPage1:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_field = Locators.first_name_field
        self.last_name_field = Locators.last_name_field
        self.postal_code_field = Locators.postal_code_field
        self.continue_button = Locators.continue_button
        self.cancel_button = Locators.cancel_button

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