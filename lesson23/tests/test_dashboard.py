import time
from lesson23.conftest import dashboard, driver

def test_click_on_zootovary_category(dashboard):
    dashboard.choose_nastilnu_igry()
    time.sleep(7)


def test_search_for_zoofood(dashboard):
    dashboard.send_text_to_search_field('Akana')
    time.sleep(10)