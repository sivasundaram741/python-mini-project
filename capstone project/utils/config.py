from selenium import webdriver

def get_driver(browser="chrome"):
    """Initialize and return the WebDriver based on the browser choice."""
    if browser.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox()
    elif browser.lower() == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Unsupported browser! Choose from 'chrome', 'firefox', or 'edge'.")
    
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver
