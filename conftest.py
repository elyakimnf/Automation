import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page_step1 import CheckoutPage1
from pages.checkout_page_step2 import CheckoutPage2
from pages.checkout_complete_page import CompleteCheckout


@pytest.fixture
def browser():
    # Set up the WebDriver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# login fixture
@pytest.fixture
def login_page(browser):
    page = LoginPage(browser)
    page.load()
    return page

# product fixture
@pytest.fixture
def product_page(browser):
    return ProductPage(browser)

# cart fixture
@pytest.fixture
def cart_page(browser):
    return CartPage(browser)

# checkout fixture
@pytest.fixture
def checkout_page_step1(browser):
    return CheckoutPage1(browser)

@pytest.fixture
def checkout_page_step2(browser):
    return CheckoutPage2(browser)

@pytest.fixture
def checkout_complete_page(browser):
    return CompleteCheckout(browser)