import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from utils.driver_factory import DriverFactory
from pages.homepage import HomePage
from pages.admin_page import AdminPage

@pytest.mark.parametrize("username, password", [
    ("Admin", "admin123"),
    ("InvalidUser", "wrongpassword")
])
def test_login(username, password):
    driver = DriverFactory('chrome').get_driver()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    try:
        login_page = LoginPage(driver)
        login_page.login(username, password)

        if username == "Admin":
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "admin-menu-selector"))
            )
            home_page = HomePage(driver)
            assert home_page.is_admin_menu_visible() is True
            home_page.click_admin_menu()

            admin_page = AdminPage(driver)
            assert admin_page.is_user_in_table(username) is True
        else:
            assert "Invalid credentials" in driver.page_source
    finally:
        driver.quit()
