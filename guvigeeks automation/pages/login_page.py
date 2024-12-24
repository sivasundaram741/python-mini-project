from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
class LoginPage(BasePage):
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Login']")
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")

    def login(self, email, password):
        self.find_element(self.EMAIL_FIELD).send_keys(email)
        self.find_element(self.PASSWORD_FIELD).send_keys(password)
        self.click_element(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.find_element(self.ERROR_MESSAGE).text