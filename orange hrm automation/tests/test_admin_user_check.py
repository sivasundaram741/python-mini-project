import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver_factory import DriverFactory
pytest.fixture()
class AdminPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_admin_page(self):
        admin_menu = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/web/index.php/admin/viewAdminModule']"))
        )
        admin_menu.click()

    def search_user(self, username):
        search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='user management']"))
        )
        search_box.send_keys(username)

        search_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        search_button.click()

    def is_user_present(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".oxd-table"))
        )
        rows = self.driver.find_elements(By.CSS_SELECTOR, ".oxd-table-row")
        for row in rows:
            if username in row.text:
                return True
        return False


def test_verify_admin_user():
    driver = DriverFactory('chrome').get_driver()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    try:
        # Login Page
        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Navigate to Admin Page
        admin_page = AdminPage(driver)
        admin_page.navigate_to_admin_page()

        # Search for Admin User
        admin_page.search_user("Admin")

        # Verify Admin User is Present
        assert admin_page.is_user_present("Admin"), "Admin user not found in the system users table."
    finally:
        driver.quit()
