import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()  # Adjust if using another browser
    driver.maximize_window()
    yield driver
    driver.quit()
