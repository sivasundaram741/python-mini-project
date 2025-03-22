def test_page_title(driver):
    """Test whether the webpage title is correct."""
    expected_title = "GUVI | Learn to code in your native language"
    assert driver.title == expected_title, f"Expected '{expected_title}', but got '{driver.title}'"
