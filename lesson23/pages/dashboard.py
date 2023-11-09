from lesson23.pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class Dashboard(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.catalog_locator = ('xpath', '//button[@id="fat-menu"]')
        self.catalog_zootovary_locator = ('xpath', '//ul[@class="menu-categories ng-star-inserted"]/li[@class="menu-categories__item ng-star-inserted"]/a[@href="https://rozetka.com.ua/ua/zootovary/c3520929/"][1]')
        #self.zootovary_locator = ('xpath', '//a[text()="Зоотовари"][1]/span')
        self.search_locator = ('xpath', '//input[@name="search"]')

    def choose_zootovary_category(self):
        self._click(self.catalog_locator)
        self._click(self.catalog_zootovary_locator)

    def send_text_to_search_field(self, text):
        element = self.wait_until_element_appears(self.search_locator)
        element.send_keys(text)
        element.send_keys(Keys.ENTER)

