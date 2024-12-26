import pytest
from utils.driver_factory import DriverFactory

def test_home_url():
    driver = DriverFactory('chrome').get_driver()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    assert driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    
    driver.quit()
