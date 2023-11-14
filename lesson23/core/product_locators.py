from lesson23.core.base_locators import BaseLocator

class ProductLocator(BaseLocator):
    def __init__(self):
        super().__init__()
        self.buy_button_locator = ('xpath', '//div[@class="product-order"]//span[@class="btn-content"][text()="Купити"]')
        self.in_stock_locator = ('xpath', '//div[@class="product-header__availability"][contains(text(),"В наявності")]')
