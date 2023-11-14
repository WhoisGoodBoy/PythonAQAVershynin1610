from lesson23.core.base_locators import BaseLocator


class CategoryLocator(BaseLocator):
    def __init__(self):
        super().__init__()
        self.filter_cheap_first_locator = ('xpath', '//span[@data-sort-href="/nastilni-ihry/simeini/filter/sort_price=ASC/"]')
        self.first_category_result = ('xpath', '//a[@class="catalogCard-image "]')
        self.filter_by_stock_locator = ('xpath', '//span[@class="filter-title"][text()="В наявності"]/../span[@class="checkbox"]')
        self.pagination_locator = ('xpath', '//span[@class="pager__item-text"][text()="2"]')
