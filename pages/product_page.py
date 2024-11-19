from data.helper import Locators


class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_button = Locators.add_to_cart_button
        self.shopping_cart = Locators.shopping_cart

    # func for add single item to cart
    def add_products(self):
        self.driver.find_element(*self.add_to_cart_button).click()

    # func for add multiple item to cart
    def add_product_to_cart(self, index):
        buttons = self.driver.find_elements(*self.add_to_cart_button)
        buttons[index].click()

    # open shopping cart
    def go_to_cart(self):
        self.driver.find_element(*self.shopping_cart).click()