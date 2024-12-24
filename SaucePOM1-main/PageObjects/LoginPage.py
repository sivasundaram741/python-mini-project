from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Import the data and locators
from TestData.data import SauceLabsData
from TestLocators.locators import SauceLabsLocators

class SauceLoginPage:
    
    # Now 'self' is included to make it an instance method
    def __init__(self, driver):
        self.driver = driver  # Store the driver instance

    def login(self):
        # Use WebDriverWait to wait for the username input field to be visible and enabled
        username_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, SauceLabsLocators.username_locator))
        )
        username_input.send_keys(SauceLabsData.username)

        # Similarly, wait for the password input field to be visible and enabled
        password_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, SauceLabsLocators.password_locator))
        )
        password_input.send_keys(SauceLabsData.password)

        # Wait for the login button to be clickable
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, SauceLabsLocators.login_button_locator))
        )
        login_button.click()
        
        # Optionally, you can return a boolean or a value indicating login success
        return True
