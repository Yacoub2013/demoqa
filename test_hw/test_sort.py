import pytest

from pages.webtables import Webtables
from conftest import browser
import time


def test_modal_dialogs(browser):
    page = Webtables(browser)
    page.visit()

    assert page.first_line.get_text() == 'Cierra'

    page.btn_fn.click()
    assert page.first_line.get_text() == 'Alden'

    page.btn_fn.click()
    assert page.first_line.get_text() == 'Kierra'





