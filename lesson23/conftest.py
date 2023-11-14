from selenium.webdriver import Chrome
import pytest
from lesson23.pages.dashboard import Dashboard
from lesson23.pages.category_page import CategoryPage
from lesson23.pages.subcategory import Subcategory
from lesson23.pages.product_page import ProductPage


@pytest.fixture
def driver():
    driver = Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def dashboard(driver):
    driver.get('https://geekach.com.ua/')
    yield Dashboard(driver)

@pytest.fixture
def category(driver):
    driver.get('https://geekach.com.ua/nastilni-ihry/')
    yield CategoryPage(driver)

@pytest.fixture
def sub_category(driver):
    driver.get('https://rozetka.com.ua/ua/food_for_cats/c1461212/')
    yield Subcategory(driver)


@pytest.fixture
def product(driver):
    driver.get('https://geekach.com.ua/liut-krovi-blood-rage/')
    driver.add_cookie({'name':'flag', 'value':'red'})
    print(f'cookie _ga:{driver.get_cookie("flag")}')
    driver.execute_script('window.localStorage["some stuff to store"] = "Gem"')
    print(driver.execute_script('return window.localStorage["lastExternalReferrer"];'))
    return ProductPage(driver)