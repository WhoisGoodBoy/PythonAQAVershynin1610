import time

from lesson23.pages.base_page import BasePage
from lesson23.pages.product_page import ProductPage
from lesson23.core.category_locator import CategoryLocator


class CategoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CategoryLocator()

    def got_to_first_element(self):
        self._click(self.locators.first_category_result)
        return ProductPage(self._driver)

    def filter_by_stock(self):
        self._click(self.locators.filter_by_stock_locator)

    def go_to_second_pagination_page(self):
        self._click(self.locators.pagination_locator)







