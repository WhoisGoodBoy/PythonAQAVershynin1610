from lesson23.pages.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.buy_button = ('xpath', '//div[@class="product-order"]//span[@class="btn-content"][text()="Купити"]')
        self.in_stock = ('xpath', '//div[@class="product-header__availability"][contains(text(),"В наявності")]')


    def click_on_buy_button(self):
        self._click(self.buy_button)

    def return_buy_button(self):
        return self.wait_until_element_appears(self.buy_button)

    def return_in_stock_span(self):
        return self.wait_until_element_appears(self.in_stock)