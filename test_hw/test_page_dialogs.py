import time

from pages.modal_dialogs import ModalDialogs
from conftest import browser


#def test_modal_dialogs(browser):
    #modal_dialogs = ModalDialogs(browser)
    #modal_dialogs.visit()
    #assert modal_dialogs.widgest.check_count_elements(5)


def test_navigator_modal(browser):
    navigator_modal = ModalDialogs(browser)
    navigator_modal.visit()
    navigator_modal.refresh()
    navigator_modal.tool_icon.click()
    navigator_modal.back()
    browser.set_window_size(900, 400)
    navigator_modal.forward()
    time.sleep(5)
    navigator_modal.title.check_count_elements()
