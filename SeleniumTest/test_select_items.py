import time
import pytest
from data.test_data import User

@pytest.mark.parametrize("num_products", [1, 2, 3, 4])
def test_add_multiple_product_to_cart(login_page, product_page, cart_page, num_products):
    # User login
    login_page.login(User.username, User.password)
    time.sleep(2)

    # Add specified number of products to cart
    for i in range(num_products):
        product_page.add_product_to_cart(i)
    time.sleep(2)

    # Verify that the cart contains the item
    product_page.go_to_cart()
    cart_items = cart_page.get_cart_items()
    assert len(cart_items) == num_products
    time.sleep(5)

