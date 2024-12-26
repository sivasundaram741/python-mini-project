from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@pytest.fixture()
def test_username_field_visible(driver):
    try:
        # Wait for the username field to be visible
        username_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "username"))  # Replace 'username' with the correct locator
        )
        assert username_field.is_displayed(), "Username field is not visible"
    except Exception as e:
        driver.save_screenshot("username_field_error.png")
        raise AssertionError(f"Test failed due to: {e}")

