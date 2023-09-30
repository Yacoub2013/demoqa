import time

from selenium.webdriver import ActionChains
from conftest import browser
from pages.slader import Slider


def test_slider(browser):
    page = Slider(browser)
    page.visit()
    action_chains = ActionChains(browser)
    action_chains.drag_and_drop_by_offset(page.slider.find_element(), 0, 100).perform()
    time.sleep(5)
    assert page.table.get_dom_attribute('value') == '50'
