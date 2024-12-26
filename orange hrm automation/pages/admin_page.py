from selenium.webdriver.common.by import By

class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_user_button = (By.XPATH, '//button[text()="Add User"]')
        self.user_table = (By.XPATH, '//table[@id="userListTable"]')

    def click_add_user_button(self):
        self.driver.find_element(*self.add_user_button).click()

    def is_user_in_table(self, username):
        table = self.driver.find_element(*self.user_table)
        rows = table.find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            if username in row.text:
                return True
        return False
