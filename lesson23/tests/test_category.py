import time

from lesson23.conftest import dashboard, driver, category


def test_go_to_cats_food(dashboard):
    category_nastilny_igry = dashboard.choose_nastilnu_igry()
    category_nastilny_igry.got_to_first_element()

def test_filter_by_stock_and_click(category):
    category.filter_by_stock_locator()
    category.got_to_first_element()
    time.sleep(5)

def test_go_to_second_page(category):
    category.go_to_second_pagination_page()
    time.sleep(5)
    product = category.got_to_first_element()
    product.click_on_buy_button()

