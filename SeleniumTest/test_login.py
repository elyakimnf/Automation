from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
import pytest
import time
from pages.login_page import LoginPage
from data.test_data import URL, User


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_login(driver):
    user_login = LoginPage(driver)
    user_login.login_page(URL.base_url)
    user_login.fill_username(User.USERNAME)
    user_login.fill_password(User.PASSWORD)
    time.sleep(1)
    user_login.click_login()
    time.sleep(5)

#
#
# try :
#     WebDriverWait(driver, 10).until(
#         ec.visibility_of_element_located((By.ID, "login_button_container"))
#     )
# except TimeoutException:
#     driver.quit()
#
# driver.find_element(By.ID, "user-name").send_keys("standard_user")
# driver.find_element(By.ID, "password").send_keys("secret_sauce")
# driver.find_element(By.ID, "login-button").click()
# time.sleep(5)

# driver.quit()
