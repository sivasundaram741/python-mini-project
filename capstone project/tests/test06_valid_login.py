from pages.login_page import LoginPage

def test_valid_login(driver):
    """Test logging in with valid credentials."""
    login_page = LoginPage(driver)
    login_page.navigate()
    login_page.login("valid_email@example.com", "valid_password")
    assert "dashboard" in driver.current_url, "Valid login failed!"
    login_page.logout()