from lesson23.pages.base_page import BasePage


class Subcategory(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.header_locator = '//h1/text()'
        self.product_locator = '//div[@class="goods-tile__content"][1]'


    def click_on_product(self):
        self._click(('xpath', self.product_locator))