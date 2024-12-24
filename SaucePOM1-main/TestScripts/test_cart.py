import pytest
from PageObjects.inventory_page import InventoryPage
@pytest.fixture()
def test_add_to_cart(driver):
    inventory_page = InventoryPage(driver)
    products = inventory_page.get_random_products()
    assert len(products) == 4
