from selenium.webdriver.common.by import By

class CompleteCheckout:
    def __init__(self, driver):
        self.driver = driver
        self.success_message = (By.CLASS_NAME, "complete-header")
        self.home_button = (By.ID, "back-to-products")

    # Success checkout
    def success_message(self):
        return self.driver.find_element(*self.success_message).text

    # Back to product page
    def back_home(self):
        self.driver.find_element(*self.home_button).click()
