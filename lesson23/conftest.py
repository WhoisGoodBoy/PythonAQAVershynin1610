from selenium.webdriver import Chrome
import pytest
from lesson23.pages.dashboard import Dashboard



@pytest.fixture
def driver():
    driver = Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def dashboard(driver):
    driver.get('https://rozetka.com.ua/ua/')
    yield Dashboard(driver)
