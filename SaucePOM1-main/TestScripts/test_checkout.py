from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# importing the SauceLoginPage class
from PageObjects.LoginPage import SauceLoginPage
from PageObjects.checout_page import SauceCheckoutPage
# importing test data and pytest
from TestData.data import SauceLabsData
import pytest

class TestSauceCheckout:

    # Booting Method (Fixture)
    @pytest.fixture()
    def booting_function(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_checkout(self, booting_function):
        self.driver.get(SauceLabsData.url)

        # Instantiate the SauceCheckoutPage with the driver
        checkout_page = SauceCheckoutPage(self.driver)
        
        # Add items to the cart
        checkout_page.add_items_to_cart()

        # Proceed to checkout
        checkout_page.proceed_to_checkout()

        # Fill in the checkout information
        checkout_page.fill_checkout_information()

        # Complete the checkout
        confirmation_message = checkout_page.complete_checkout()

        # Assert that the checkout was successful
        assert "Thank you for your order" in confirmation_message
        print("SUCCESS: Checkout completed!")
