from data.helper import Locators


class CheckoutPage2:
    def __init__(self, driver):
        self.driver = driver
        self.item_1_details = Locators.item_details
        self.finish_button = Locators.finish_button
        self.cancel_button = Locators.cancel_button

    # user view product details
    def view_details(self):
        self.driver.find_element(*self.item_1_details).click()

    # user finish checkout
    def finish_checkout(self):
        self.driver.find_element(*self.finish_button).click()

    # user cancel checkout
    def cancel_checkout(self):
        self.driver.find_element(*self.cancel_button).click()
