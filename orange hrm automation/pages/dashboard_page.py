from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.dashboard_widget = (By.XPATH, '//div[@class="dashboard-widget"]')

    def is_dashboard_widget_visible(self):
        return self.driver.find_element(*self.dashboard_widget).is_displayed()
