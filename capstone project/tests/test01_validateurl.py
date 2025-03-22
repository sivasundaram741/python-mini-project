import pytest
from pages.home_page import HomePage

def test_url_is_valid(driver):
    """Test whether the website URL is valid."""
    home_page = HomePage(driver)
    home_page.navigate()
    assert home_page.driver.current_url == HomePage.URL, "URL validation failed!"
