import pytest

from pages.modal_dialogs import ModalDialogs
from conftest import browser
import time


def test_modal_dialogs(browser):
    page = ModalDialogs(browser)
    if not page.code_status():
        pytest.skip(reason=f"Страница {page.base_url} недоступна")
    page.visit()
    page.small_modal.click()
    time.sleep(5)
    page.small_modal_close.click()
    time.sleep(5)
    page.large_modal.click()
    time.sleep(5)
    page.large_modal_close.click()
    time.sleep(5)




