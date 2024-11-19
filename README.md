# Selenium Automation Project

This project contains automated test scripts for [SauceDemo](https://www.saucedemo.com/) using Selenium with Python. 
The project is structured to follow best practices, including Page Object Model (POM) and reusable test cases.

---

##**Setup Instructions**##
1. **Prerequisites**
   - Install Python (version 3.8 or later).
   - Install Google Chrome or a browser of your choice.
   - Install ChromeDriver (match the version of your browser).
2. **Install Dependencies**
   - Install all required Python packages using pip:
     ```bash
     pip install -r requirements.txt
   - If requirements.txt is not set up yet, add the following manually:
     ```bash
     pip install selenium pytest

4. **Run Tests**
   - Run all tests in the project using Pytest:
     ```bash
     pytest tests/
   - Run a specific test file:
     ```bash
     pytest tests/test_login.py


---

## **Project Test**

1. **Login Tests**:
   - Valid and invalid login scenarios with assertions.

2. **Select Items Tests**:
   - Test cases for adding 1, 2, 3, and 4 products to the cart with verification.

3. **Checkout Test**:
   - Complete workflow from login to checkout.

4. **Helper File**:
   - Storage for element locators to ensure maintainability.

4. **Test Data File**:
   - Storage for test data to ensure maintainability.

---

## **Project Structure**

```plaintext
project-root/
├── data/
│   ├── helper.py                 # Storage for element locators
│   ├── test_data.py              # Storage for test data
├── pages/
│   ├── cart_page.py              # Page class for cart functionality
│   ├── login_page.py             # Page class for login functionality
│   ├── checkout_page_step1.py    # Page class for checkout functionality
│   ├── checkout_page_step2.py    # Page class for checkout functionality
│   ├── checkout_complete_page.py # Page class for checkout functionality
│   ├── product.py                # Base class for product inventory functionality
├── SeleniumTest/
│   ├── test_login.py             # Test cases for login functionality
│   ├── test_select_items.py      # Test cases for adding products to cart
│   ├── test_checkout.py          # End-to-end checkout test
├── .gitignore                  # Files and folders to ignore
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
```
---

##**Key Features in Code**##
1. Reusable Page Objects:
   Page classes are created for login, cart, and checkout pages in the pages/ folder.

2. Assertions:
   Test scripts include meaningful assertions to verify expected outcomes.
   
4. Modular Design:
   Common locators are stored in helpers/helper.py for easy updates and reusability.
