from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException  # Add this import
from TestLocators.locators import SauceLabsLocators

class SauceCheckoutPage:

    def __init__(self, driver):
        self.driver = driver  # Store the driver instance

    def add_items_to_cart(self):
     try:
        # Wait for the "Add to Cart" button to be visible and clickable
        item_button = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.ID, SauceLabsLocators.add_to_cart_button_locator))
        )
        item_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.ID, SauceLabsLocators.add_to_cart_button_locator))
        )
        item_button.click()
        print("Item added to cart")
     except TimeoutException:
        print("Timeout occurred while trying to click the 'Add to Cart' button")
        raise


    # Optionally, add more items if needed
    # You can repeat the above steps to add other items to the cart.


    def proceed_to_checkout(self):
        # Click the 'Cart' button to go to the cart page
        cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, SauceLabsLocators.cart_button_locator))
        )
        cart_button.click()

        # Proceed to checkout
        checkout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, SauceLabsLocators.checkout_button_locator))
        )
        checkout_button.click()

    def fill_checkout_information(self):
        # Fill in the required fields (e.g., name, address)
        first_name_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, SauceLabsLocators.first_name_locator))
        )
        first_name_input.send_keys("John")

        last_name_input = self.driver.find_element(By.ID, SauceLabsLocators.last_name_locator)
        last_name_input.send_keys("Doe")

        zip_code_input = self.driver.find_element(By.ID, SauceLabsLocators.zip_code_locator)
        zip_code_input.send_keys("12345")

    def complete_checkout(self):
        # Submit the checkout form
        continue_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, SauceLabsLocators.continue_button_locator))
        )
        continue_button.click()

        # Optionally, wait for the confirmation page to load
        confirmation_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, SauceLabsLocators.confirmation_message_locator))
        )
        return confirmation_message.text
