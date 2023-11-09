from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.wheel_actions import WheelActions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


def test_01():
    driver = Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('https://hard.rozetka.com.ua/ua/ssd/c80109/')
    checkbox_adata_locator = '//a[@data-id="ADATAA"]'
    checkbox_adata = driver.find_element('xpath', checkbox_adata_locator)
    checkbox_adata.click()
    #time.sleep(5)

def test_02():
    driver = Chrome()
    driver.maximize_window()
    web_driver_wait = WebDriverWait(driver, 10)
    driver.get('https://hard.rozetka.com.ua/ua/ssd/c80109/')
    checkbox_adata_locator = '//a[@data-id="ADATAA"]'
    checkbox_adata = web_driver_wait.until(EC.presence_of_element_located(('xpath', checkbox_adata_locator)))
    checkbox_adata.click()