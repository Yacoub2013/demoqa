import time
from conftest import browser
from pages.text_box import TextBox


def test_text_box(browser):
    page = TextBox(browser)
    page.visit()
    page.full_name.send_keys('GHMMFGggfg')
    time.sleep(5)
    page.current_address.send_keys('dsfsdggffgdfdfg.fg')
    time.sleep(5)
    page.submit.click()
    time.sleep(5)

    assert page.name_down.get_text() == 'Name:GHMMFGggfg'
    time.sleep(5)
    assert page.current_address_down.get_text() == "Current Address:dsfsdggffgdfdfg.fg"
    time.sleep(5)



