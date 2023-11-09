from lesson23.pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from lesson23.pages.category_page import CategoryPage


class Dashboard(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.catalog_locator = ('xpath', '//a[@href="/nastilni-ihry/"]')
        #self.catalog_zootovary_locator = ('xpath', '//ul[@class="menu-categories ng-star-inserted"]/li[@class="menu-categories__item ng-star-inserted"]/a[@href="https://rozetka.com.ua/ua/zootovary/c3520929/"][1]')
        #self.zootovary_locator = ('xpath', '//a[text()="Зоотовари"][1]/span')
        self.search_locator = ('xpath', '//input[@class="search__input"]')

    def choose_nastilnu_igry(self):
        self._click(self.catalog_locator)
        return CategoryPage(self._driver)

    def send_text_to_search_field(self, text):
        element = self.wait_until_element_appears(self.search_locator)
        element.send_keys(text)
        element.send_keys(Keys.ENTER)

