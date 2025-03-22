from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    URL = "https://www.guvi.in"
    LOGIN_BTN = (By.XPATH, "//a[contains(text(),'Login')]")
    SIGNUP_BTN = (By.XPATH, "//a[contains(text(),'Sign Up')]")

    def navigate(self):
        self.open_url(self.URL)

    def is_login_button_visible(self):
        return self.find_element(self.LOGIN_BTN).is_displayed()

    def is_signup_button_visible(self):
        return self.find_element(self.SIGNUP_BTN).is_displayed()
