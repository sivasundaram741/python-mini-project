from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SignUpPage(BasePage):
    URL = "https://www.guvi.in/sign-in/"
    
    NAME_FIELD = (By.ID, "name")  # Update with correct locator
    EMAIL_FIELD = (By.ID, "email")  # Update with correct locator
    PASSWORD_FIELD = (By.ID, "password")  # Update with correct locator
    SIGNUP_BUTTON = (By.XPATH, "//button[contains(text(),'Sign Up')]")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-msg")  # Update with correct locator
    SUCCESS_MESSAGE = (By.CLASS_NAME, "success-msg")  # Update with correct locator

    def navigate(self):
        """Open the signup page."""
        self.open_url(self.URL)

    def sign_up(self, name, email, password):
        """Perform the signup operation."""
        self.find_element(self.NAME_FIELD).send_keys(name)
        self.find_element(self.EMAIL_FIELD).send_keys(email)
        self.find_element(self.PASSWORD_FIELD).send_keys(password)
        self.click_element(self.SIGNUP_BUTTON)

    def get_error_message(self):
        """Capture error message on failed signup."""
        return self.find_element(self.ERROR_MESSAGE).text

    def get_success_message(self):
        """Capture success message on successful signup."""
        return self.find_element(self.SUCCESS_MESSAGE).text
