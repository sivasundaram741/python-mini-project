from pages.signup_page import SignUpPage

def test_signup_page_navigation(driver):
    """Check whether clicking Sign-Up navigates to the correct page."""
    signup_page = SignUpPage(driver)
    signup_page.navigate()
    assert "sign-in" in driver.current_url, "Sign-Up page did not load correctly!"
