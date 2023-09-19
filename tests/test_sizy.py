from conftest import browser
from pages.demoqa import DemoQa
import time


def page_size(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    browser.set_window_size(1000, 300)
    time.sleep(3)
    browser.set_window_size(1000, 1000)
