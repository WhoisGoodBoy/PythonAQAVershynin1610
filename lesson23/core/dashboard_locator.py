from lesson23.core.base_locators import BaseLocator


class DashBoardLocator(BaseLocator):
    def __init__(self):
        super().__init__()
        self.catalog_locator = ('xpath', '//a[@href="/nastilni-ihry/"]')
        self.search_locator = ('xpath', '//input[@class="search__input"]')
        self.blockbusters = ('xpath', '//a[text()="Хіти продажу"]')
        self.sell = ('xpath', '//a[text()="Розпродаж"]')
        self.new = ('xpath', '//a[text()="Новинки"]')
