from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://www.guvi.in/sign-in/"
    EMAIL_FIELD = (By.ID, "email")  # Update with correct locator
    PASSWORD_FIELD = (By.ID, "password")  # Update with correct locator
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Login')]")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-msg")  # Update with correct locator
    LOGOUT_BUTTON = (By.XPATH, "//a[contains(text(),'Logout')]")  # Update with correct locator

    def navigate(self):
        """Open the login page."""
        self.open_url(self.URL)

    def login(self, email, password):
        """Perform login operation."""
        self.find_element(self.EMAIL_FIELD).send_keys(email)
        self.find_element(self.PASSWORD_FIELD).send_keys(password)
        self.click_element(self.LOGIN_BUTTON)

    def get_error_message(self):
        """Capture error message on failed login."""
        return self.find_element(self.ERROR_MESSAGE).text

    def logout(self):
        """Logout from the account."""
        self.click_element(self.LOGOUT_BUTTON)
