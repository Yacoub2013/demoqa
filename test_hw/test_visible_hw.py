from conftest import browser
from pages.accordion import Accordion
import time


def test_visible_accordion(browser):
    page_accordion = Accordion(browser)
    page_accordion.visit()
    assert page_accordion.text1.visible()
    assert page_accordion.heading.click()
    time.sleep(2)
    assert not page_accordion.text1.visible()


def test_visible_default(browser):
    page_accordion = Accordion(browser)
    page_accordion.visit()
    assert page_accordion.element_1.visible()
    assert page_accordion.element_2.visible()
    assert page_accordion.element_3.visible()

