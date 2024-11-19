import time

from data.test_data import User
from conftest import login_page

def test_success_login(login_page):
    login_page.login(User.username, User.password)
    assert "Swag Labs" in login_page.driver.title
    time.sleep(2)

def test_invalid_login(login_page):
    login_page.login(User.username, "wrong_password")
    error_message = login_page.error_login()
    time.sleep(2)
    assert "Username and password do not match any user in this service" in error_message