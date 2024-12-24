import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from utils.config import BASE_URL,LOGIN_URL
# Test Case 3: Verify Login button visibility and clickability
def test_login_button(browser):
    browser.get(BASE_URL)
    login_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Login']"))
    )
    assert login_button.is_displayed(), "Login button is not visible."
    assert login_button.is_enabled(), "Login button is not clickable."
# Test Case 7: Verify invalid login error message
def test_invalid_login(browser):
    browser.get(LOGIN_URL)
    login_page = LoginPage(browser)
    login_page.login("invalid_email@example.com", "wrong_password")
    error_message = login_page.get_error_message()
    assert error_message, "Error message is not displayed for invalid login."