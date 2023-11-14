from lesson23.conftest import dashboard, driver, category, sub_category, product
import time


def test_buy_product(product):
    product.click_on_buy_button()
    product.add_cookie_brownie()
    time.sleep(5)


def test_product_in_stock_and_buy_button_exist(product):
    assert product.return_buy_button().text == 'Купити'
    assert product.return_in_stock_span().text == 'В наявності'