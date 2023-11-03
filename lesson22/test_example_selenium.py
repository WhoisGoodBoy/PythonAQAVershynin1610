from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.wheel_actions import WheelActions
from selenium.webdriver.common.action_chains import ActionChains

import time

def test_01():
    driver = Chrome()
    driver.get('https://google.com')
    search_field_locator = '//textarea[@type="search"]'
    element = driver.find_element(by='xpath', value=search_field_locator)
    element.send_keys('погода київ')
    element.send_keys(Keys.ENTER)
    second_page_weather_status_locator = "wob_dc"
    second_page_weather_status = driver.find_element('id',second_page_weather_status_locator)
    assert second_page_weather_status.text == 'Ясно'
    time.sleep(5)


def test_02():
    driver = Chrome()
    driver.get('https://google.com')
    driver.maximize_window()
    search_field_locator = '//textarea[@type="search"]'
    element = driver.find_element(by='xpath', value=search_field_locator)
    element.send_keys('погода київ')
    element.send_keys(Keys.ENTER)
    unian = driver.find_element('xpath', "//h3[text()='Погода Київ, прогноз погоди у Київ']")
    action = ActionChains(driver)
    action.move_to_element(to_element=unian)
    action.perform()
    time.sleep(5)
    action.scroll_by_amount(delta_x=0,delta_y=10000)
    action.perform()
    time.sleep(5)
    meteolabs = driver.find_element('xpath', "//h3[text()='Погода в Киеве']")

    action.move_to_element(to_element=meteolabs)
    action.perform()

#    meteolabs = driver.find_element('xpath', "//h3[text()='Погода в Києві на 14 днів - meteolabs.com.ua']")
    meteolabs.click()
    time.sleep(5)
    '''
    go_to_acuweather_locator = "//h3[text()='Київ, Київ, Україна Прогноз погоди на 3 дні']/.."
    go_to_acuweather = driver.find_element('xpath',go_to_acuweather_locator)
    go_to_acuweather.click()
    bad_air_quality_locator = '//span[text()="Якість повітря"]/following-sibling::span'
    bad_air_quality = driver.find_element('xpath', bad_air_quality_locator)
    assert bad_air_quality.text == 'Погано'

    time.sleep(5)'''

def test_03():
    driver = Chrome()
    driver.get('https://hard.rozetka.com.ua/ua/ssd/c80109/')
    checkbox_adata_locator = '//a[@data-id="ADATA"]'
    checkbox_adata = driver.find_element('xpath', checkbox_adata_locator)
    checkbox_adata.click()
    time.sleep(5)