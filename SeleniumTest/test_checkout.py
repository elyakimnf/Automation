import time
from data.test_data import User


def test_checkout(login_page, product_page, cart_page, checkout_page_step1, checkout_page_step2, checkout_complete_page):
    # User login
    login_page.login(User.username, User.password)
    time.sleep(2)

    # Select product - add to cart
    product_page.add_products()
    time.sleep(2)

    # Verify that the cart contains the item
    product_page.go_to_cart()
    time.sleep(2)

    # Checkout the items
    cart_page.user_checkout()
    time.sleep(2)

    # Input checkout information (step one)
    checkout_page_step1.checkout_info(User.first_name, User.last_name, User.postal_code)
    time.sleep(2)
    checkout_page_step1.continue_checkout()
    time.sleep(2)

    # Checkout overview (step2)
    checkout_page_step2.finish_checkout()
    time.sleep(2)

    # Success checkout
    message = checkout_complete_page.success_checkout()
    assert "Thank you for your order!" in message
    time.sleep(2)

    # # Back to product page (optional)
    # checkout_complete_page.back_home()
    # time.sleep(5)