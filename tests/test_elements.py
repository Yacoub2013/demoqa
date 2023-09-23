from conftest import browser
from pages.elements_page import ElementsPage
from pages.elemnt_chekbox import Checkbox


def test_find_elements(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()
    assert elements_page.btns_first_menu.check_count_elements(9)  # проверяет что их 9 шт


def test_count_checkbox(browser):
    elements_page_checkbox = Checkbox(browser)
    elements_page_checkbox.visit()

    assert elements_page_checkbox.checkbox.check_count_elements(1)
    elements_page_checkbox.btn_expand_all.click()

    assert elements_page_checkbox.checkbox.check_count_elements(17)
    browser.refresh()

    assert elements_page_checkbox.checkbox.check_count_elements(1)






