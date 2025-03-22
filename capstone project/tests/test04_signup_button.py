from pages.home_page import HomePage

def test_signup_button_visible(driver):
    """Check whether the Sign-Up button is visible."""
    home_page = HomePage(driver)
    home_page.navigate()
    assert home_page.is_signup_button_visible(), "Sign-Up button is not visible!"

def test_signup_button_clickable(driver):
    """Check whether the Sign-Up button is clickable."""
    home_page = HomePage(driver)
    home_page.navigate()
    home_page.click_element(home_page.SIGNUP_BTN)
    assert "sign-in" in driver.current_url, "Sign-Up button is not clickable!"
