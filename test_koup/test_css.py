from pages.elements_page import ElementsPage
from conftest import browser


def test_flex_menu(browser):
    page_1 = ElementsPage(browser)
    page_1.visit()

    assert page_1.block_menu.check_css('flex', '0 0 25%')
    assert page_1.block_menu.check_css('max-width', '25%')
    browser.set_window_size(650, 1000)
    assert page_1.block_menu.check_css('flex', '0 0 100%')
    assert page_1.block_menu.check_css('max-width', '100%')
    browser.set_window_size(1000, 1000)

