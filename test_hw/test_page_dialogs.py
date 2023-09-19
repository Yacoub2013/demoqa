from pages.modal_dialogs import ModalDialogs
from conftest import browser


def test_modal_dialogs(browser):
    modaldialogs = ModalDialogs(browser)
    modaldialogs.visit()
    assert modaldialogs.widgest.check_count_elements(5)

