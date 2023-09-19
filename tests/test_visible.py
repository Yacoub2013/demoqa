import time
from pages.elements_page import ElementsPage
from conftest import browser


def test_visible_btn_sidebar(browser):
    element_page = ElementsPage(browser)
    element_page.visit()
    # element_page.btn_sidebar_first.click()
    # time.sleep(3)
    # assert element_page.btn_siderbar_first_textbox.exist()
    assert element_page.btn_siderbar_first_textbox.visible()
    # assert not element_page.btn_siderbar_first_textbox.visible()


def test_not_visible_btn_siderbar(browser):
    element_page = ElementsPage(browser)
    element_page.visit()
    assert element_page.btn_siderbar_first_checkbox.visible()
    element_page.btn_sidebar_first.click()
    time.sleep(2)
    assert not element_page.btn_siderbar_first_checkbox.visible()

