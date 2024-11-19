import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from data.test_data import Page

@pytest.fixture
def browser():
    # Set up the WebDriver (e.g., Chrome)
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def login_page(browser):
    # Initialize and load the LoginPage using the browser instance
    login_page = LoginPage(browser)
    login_page.load(Page.url)  # Navigate to the login page URL
    return login_page
