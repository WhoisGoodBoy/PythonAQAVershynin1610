from lesson23.conftest import dashboard, driver, category, sub_category
import time



def test_click_on_product(sub_category):
    sub_category.click_on_product()
    time.sleep(5)



