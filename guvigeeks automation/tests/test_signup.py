import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config import BASE_URL
# Test Case 4: Verify Sign-Up button visibility and clickability (tests/test_signup.py)
def test_signup_button(browser):
    browser.get(BASE_URL)
    signup_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Sign Up']"))
    )
    assert signup_button.is_displayed(), "Sign-Up button is not visible."
    assert signup_button.is_enabled(), "Sign-Up button is not clickable."

# Test Case 5: Verify navigation to Sign-Up page and Log-Out functionality (tests/test_signup.py)
def test_signup_navigation(browser):
    browser.get(BASE_URL)
    signup_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Sign Up']"))
    )
    signup_button.click()
    assert "sign-up" in browser.current_url, "Sign-Up page did not load."