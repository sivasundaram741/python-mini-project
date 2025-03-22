import pytest
from utils.config import get_driver
from utils.logger import get_logger

# Initialize logger
logger = get_logger()

@pytest.fixture(scope="function")
def driver():
    """Initialize WebDriver before each test and quit after test."""
    logger.info("Starting WebDriver...")
    driver = get_driver("chrome")  # Change to "firefox" or "edge" if needed
    yield driver
    logger.info("Closing WebDriver...")
    driver.quit()
