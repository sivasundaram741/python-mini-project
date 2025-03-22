from pages.login_page import LoginPage

def test_invalid_login(driver):
    """Test logging in with invalid credentials and catching the error message."""
    login_page = LoginPage(driver)
    login_page.navigate()
    login_page.login("invalid_email@example.com", "wrong_password")
    assert "Invalid credentials" in login_page.get_error_message(), "Error message is incorrect!"