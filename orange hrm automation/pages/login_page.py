from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.NAME, 'username')
        self.password_field = (By.NAME, 'password')
        self.login_button = (By.XPATH, '//button[@type="submit"]')
        self.logout_button = (By.XPATH, '//a[@href="/web/index.php/auth/logout"]')

    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def click_logout(self):
        self.driver.find_element(*self.logout_button).click()

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
        ).send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    def logout(self):
        self.click_logout()
