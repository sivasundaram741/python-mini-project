from selenium.webdriver.common.by import By
from pages.base_page import BasePage
class SignupPage(BasePage):
    SIGNUP_BUTTON = (By.XPATH, "//button[text()='Sign Up']")