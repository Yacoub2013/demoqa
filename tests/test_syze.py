import time
from conftest import browser
from pages.elements_page import ElementsPage


def test_visible_nav_bar(browser):
    element_page = ElementsPage(browser)  # создаем страницу с которой мы будем работать
    element_page.visit()
    assert not element_page.nav_bar.visible()
    browser.set_window_size(240, 320) # 767 * 1000- размер мобильной версий
    time.sleep(3)
    assert element_page.nav_bar.visible()
    browser.set_window_size(1000, 1000)
