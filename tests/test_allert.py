import time
from pages.alerts import Alerts
from conftest import browser


def test_allert(browser):
    page = Alerts(browser)
    page.visit()

    #assert not page.alert()

    #page.alert_button.click()

    # time.sleep(2)
    # assert page.alert().text == 'You clicked a button'
    # page.alert().accept()
    # assert not page.alert()

    page.confirm_button.click()
    time.sleep(2)
    page.alert().dismiss()
    assert page.confirm_result.get_text() == 'You selected Cancel'

    #page.promt_button.click()
    #time.sleep(2)
    #page.alert().send_keys('MyName')
    #page.alert().accept()
    #assert page.promt_result.get_text() == 'You entered MyName'
    #time.sleep(3)
