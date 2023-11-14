from lesson23.pages.base_page import BasePage
from lesson23.core.product_locators import ProductLocator


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ProductLocator()

    def click_on_buy_button(self):
        self._click(self.locators.buy_button_locator)

    def return_buy_button(self):
        return self.wait_until_element_appears(self.locators.buy_button_locator)

    def return_in_stock_span(self):
        return self.wait_until_element_appears(self.locators.in_stock_locator)

    def add_cookie_brownie(self):
        self._driver.add_cookie({'name':'brownie', 'value':'brown'})
        print(f'cookie brownie:{self._driver.get_cookie("brownie")}')
