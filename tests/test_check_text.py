from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
from conftest import browser


def test_page_elements(browser):
    element_page = ElementsPage(browser)
    element_page.visit()
    assert element_page.text_elements.get_text() == 'Elements'
    assert element_page.icona.exist()
    assert element_page.btn_sidebar_first.exist()
    assert element_page.btn_siderbar_first_textbox.exist()

