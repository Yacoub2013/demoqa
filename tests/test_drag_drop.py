from pages.droppable import Droppable
from conftest import browser
import time
from selenium.webdriver import ActionChains


def test_drag_and_drop(browser):
    page = Droppable(browser)
    page.visit()
    action_chains = ActionChains(browser)

    # action_chains.drag_and_drop(page.drag.find_element(), page.drop.find_element()).perform()
    # time.sleep(5)
    assert page.drag.check_css('rgba(0 0 0 0)')
    action_chains.drag_and_drop(page.drag.find_element(), page.drop.find_element()).perform()
    assert page.drag.check_css('rgba(70 130 180 1)')
    action_chains.drag_and_drop_by_offset(page.drop.find_element(), 100, 100).perform()
    assert page.drag.check_css('rgba(70 130 180 1)')
    time.sleep(5)

