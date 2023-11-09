import time

from lesson23.pages.base_page import BasePage
from lesson23.pages.product_page import ProductPage


class CategoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.first_category_result = ('xpath', '//a[@class="catalogCard-image "]')
        self.filter_by_stock_locator = ('xpath', '//span[@class="filter-title"][text()="В наявності"]/../span[@class="checkbox"]')
        self.pagination_locator = ('xpath', '//span[@class="pager__item-text"][text()="2"]')


    def got_to_first_element(self):
        self._click(self.first_category_result)
        return ProductPage(self._driver)

    def filter_by_stock(self):
        self._click(self.filter_by_stock_locator)

    def go_to_second_pagination_page(self):
        self._click(self.pagination_locator)







