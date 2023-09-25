import time
from conftest import browser
from pages.modal_dialogs import ModalDialogs


def test_navigation(browser):
    page = ModalDialogs(browser)
    page.visit()
    time.sleep(2)

    page.refresh()
    time.sleep(2)

    page.tool_icon.click()
    time.sleep(2)

    page.back()
    time.sleep(2)

    browser.set_window_size(900, 400)
    time.sleep(2)

    page.forward()
    time.sleep(2)

    assert browser.current_url == 'https://demoqa.com/'
    assert browser.title == 'DEMOQA'

    browser.set_window_size(1000, 1000)
    time.sleep(2)






