import pytest
from utils.config import BASE_URL
@pytest.mark.parametrize("url", [BASE_URL])
def test_url_validity(browser, url):
    try:
        browser.get(url)
        assert browser.current_url == url, "URL is not valid."
    except Exception as e:
        pytest.fail(f"Failed to load URL. Error: {e}")

# Test Case 2: Verify webpage title (tests/test_navigation.py)
@pytest.mark.parametrize("expected_title", ["GUVI | Learn to code in your native language"])
def test_webpage_title(browser, expected_title):
    browser.get(BASE_URL)
    assert browser.title == expected_title, "Webpage title does not match."