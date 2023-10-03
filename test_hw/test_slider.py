import time

from selenium.webdriver import ActionChains, Keys
from conftest import browser
from pages.slader import Slider


def test_slider(browser):
    page = Slider(browser)
    page.visit()
    # assert page.slider.exist()
    # assert page.inp.exist()
    #
    # while not page.inp.get_dom_attribute('value') == '50':
    #     page.slider.send_keys(Keys.ARROW_RIGHT)

    action_chains = ActionChains(browser)

    action_chains.drag_and_drop_by_offset(page.slider.find_element(), 0, 200).perform()
    time.sleep(5)
    assert page.table.get_dom_attribute('value') == '50'
