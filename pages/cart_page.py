from selenium.webdriver.common.by import By
from data.helper import Locators

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.item_details = Locators.item_details
        self.remove_item = Locators.remove_item
        self.continue_shopping = Locators.continue_shopping
        self.checkout_button = Locators.checkout_button

    # user view product details
    def view_details(self):
        self.driver.find_element(*self.item_details).click()

    # user remove product from cart
    def remove_from_cart(self):
        self.driver.find_element(*self.remove_item).click()

    # user redirect to product page
    def back_to_product(self):
        self.driver.find_element(*self.continue_shopping).click()

    # user click checkout button
    def user_checkout(self):
        self.driver.find_element(*self.checkout_button).click()

    # verify added items
    def get_cart_items(self):
        return [item.text for item in self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")]