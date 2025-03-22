from pages.home_page import HomePage

def test_login_button_visible(driver):
    """Check whether the Login button is visible."""
    home_page = HomePage(driver)
    home_page.navigate()
    assert home_page.is_login_button_visible(), "Login button is not visible!"

def test_login_button_clickable(driver):
    """Check whether the Login button is clickable."""
    home_page = HomePage(driver)
    home_page.navigate()
    home_page.click_element(home_page.LOGIN_BTN)
    assert "sign-in" in driver.current_url, "Login button is not clickable!"
