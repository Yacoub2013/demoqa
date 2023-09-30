import time

from conftest import browser
from pages.progress_bar import ProgressBar


def test_progress_bar(browser):
    page = ProgressBar(browser)
    page.visit()
    time.sleep(2)
    page.start.click()
    time.sleep(10)
    while page.progress_bar.get_dom_attribute('value') == '51':
        page.start.click()
