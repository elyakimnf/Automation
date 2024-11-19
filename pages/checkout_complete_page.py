from data.helper import Locators


class CompleteCheckout:
    def __init__(self, driver):
        self.driver = driver
        self.success_message = Locators.success_message
        self.home_button = Locators.home_button

    # Success checkout
    def success_checkout(self):
        return self.driver.find_element(*self.success_message).text

    # Back to product page
    def back_home(self):
        self.driver.find_element(*self.home_button).click()