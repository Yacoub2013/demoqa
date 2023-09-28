import time
from pages.alerts import Alerts
from conftest import browser


def test_time_allert(browser):
    page = Alerts(browser)
    page.visit()

    assert not page.alert()
    page.time_alert_button.click()
    time.sleep(10)
    assert page.alert()
    page.alert().accept()


