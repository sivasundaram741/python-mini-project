from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# importing the SauceLoginPage class
from PageObjects.LoginPage import SauceLoginPage

# importing test data and pytest
from TestData.data import SauceLabsData
import pytest

class TestSauceLogin:

    # Booting Method
    @pytest.fixture()
    def booting_function(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        yield
        self.driver.close()

    # test case for validating login
    def test_validate_login(self, booting_function):
     self.driver.get(SauceLabsData.url)
    
    # Instantiate the SauceLoginPage with the driver
     login_page = SauceLoginPage(self.driver)
    
    # Call the login method on the instantiated object
     assert login_page.login()  # Now it correctly uses self.driver in the method
     print("SUCCESS : Logged in !")


    # test case for standard user login
    def test_login_standard_user(self, booting_function):
     self.driver.get(SauceLabsData.url)
    
    # Instantiate the SauceLoginPage with the driver
     login_page = SauceLoginPage(self.driver)
    
    # Call the login method
     assert login_page.login()  # No need to pass the driver here
    


