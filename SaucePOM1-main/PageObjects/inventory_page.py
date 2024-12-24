from selenium.webdriver.common.by import By
import random

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.inventory_item = (By.CLASS_NAME, "inventory_item")
        self.cart_button = (By.CLASS_NAME, "shopping_cart_badge")

    def get_random_products(self, count=4):
        items = self.driver.find_elements(*self.inventory_item)
        selected_items = random.sample(items, count)
        products = []
        for item in selected_items:
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            price = item.find_element(By.CLASS_NAME, "inventory_item_price").text
            products.append((name, price))
        return products
