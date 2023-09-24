import time
from conftest import browser
from pages.form_page import FormPage
from pages.text_box import TextBox


def test_clear(browser):
    text_box = TextBox(browser)
    text_box.visit()

    text_box.full_name.send_keys('tester')
    time.sleep(2)
    text_box.full_name.click()
    time.sleep(2)
    assert text_box.full_name.get_text() == ''
