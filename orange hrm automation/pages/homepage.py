from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.admin_menu = (By.XPATH, '//a[@href="/web/index.php/admin/viewAdminModule"]')
        self.pim_menu = (By.XPATH, '//a[@href="/web/index.php/pim/viewPimModule"]')

    def is_admin_menu_visible(self):
        return self.driver.find_element(*self.admin_menu).is_displayed()

    def is_pim_menu_visible(self):
        return self.driver.find_element(*self.pim_menu).is_displayed()

    def click_admin_menu(self):
        self.driver.find_element(*self.admin_menu).click()

    def click_pim_menu(self):
        self.driver.find_element(*self.pim_menu).click()
