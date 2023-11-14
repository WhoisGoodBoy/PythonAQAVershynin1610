from lesson23.pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from lesson23.pages.category_page import CategoryPage
from lesson23.core.dashboard_locator import DashBoardLocator


class Dashboard(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = DashBoardLocator()
    def choose_nastilnu_igry(self):
        self._click(self.locators.catalog_locator)
        return CategoryPage(self._driver)

    def send_text_to_search_field(self, text):
        element = self.wait_until_element_appears(self.locators.search_locator)
        element.send_keys(text)
        element.send_keys(Keys.ENTER)

