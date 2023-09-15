from pages import elements_page
from pages.elements_page import ElementsPage
from conftest import browser

def test_page_elements(browser):
    page = ElementsPage(browser)
    page.visit()
    assert elements_page.text_elements.get_text() =='Elements'


