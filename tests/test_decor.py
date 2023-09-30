import pytest
from pages.demoqa import DemoQa
from conftest import browser
import time
from selenium.webdriver import ActionChains
from pages.radio_button import RadioButton


@pytest.mark.skip
def test_decor(browser):
    page = DemoQa(browser)
    page.visit()

    assert page.elements_1.check_count_elements(6)

    for element in page.elements_1.find_elements():
        assert element.text != ''


#@pytest.mark.skipif(True, reason='просто пропуск')
def test_radio_button(browser):
    page1 = RadioButton(browser)
    if not page1.code_status():
        pytest.skip(reason=f"Страница {page1.base_url} недоступна")
    page1.visit()

    page1.yes.click()
    assert page1.text_yes.get_text() == 'You have selected Yes'

    page1.impressive.click()
    assert page1.text_yes.get_text() == 'You have selected Impressive'

    assert 'disabled' in page1.no.get_dom_attribute('class')

