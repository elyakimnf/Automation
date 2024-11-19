from selenium.webdriver.common.by import By

class Locators:
    # Login Page
    username_field = (By.ID, "user-name")
    password_field = (By.ID, "password")
    login_button = (By.ID, "login-button")
    error_login_message = (By.CLASS_NAME, "error-message-container")
    # Product page
    add_to_cart_button = (By.CLASS_NAME, "btn_inventory")
    shopping_cart = (By.XPATH, '//*[@id="shopping_cart_container"]/a')
    # Cart page
    item_details = (By.CLASS_NAME, "inventory_item_name")
    remove_item = (By.CLASS_NAME, "btn btn_secondary btn_small cart_button")
    continue_shopping = (By.ID, "continue-shopping")
    checkout_button = (By.ID, "checkout")
    # Checkout page
    first_name_field = (By.ID, "first-name")
    last_name_field = (By.ID, "last-name")
    postal_code_field = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")
    cancel_button = (By.ID, "cancel")
    finish_button = (By.ID, "finish")
    # complete checkout page
    success_message = (By.CLASS_NAME, "complete-header")
    home_button = (By.ID, "back-to-products")
