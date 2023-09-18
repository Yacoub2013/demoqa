from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
from conftest import browser
from selenium.common import NoSuchElementException


def test_text_elements(browser):
    text_basement = ElementsPage(browser)
    text_basement.visit()
    assert text_basement.basement.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'


def test_text_centre(browser):
    text_centre = DemoQa(browser)
    text_centre.visit()
    text_centre.elements.click()
    page = ElementsPage(browser)
    assert page.centre.get_text() == 'Please select an item from left to start practice.'

