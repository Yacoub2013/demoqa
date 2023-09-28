import time

import pytest
from pages.base_page import BasePage
from pages.accordion import Accordion
from pages.alerts import Alerts
from pages.browser_tap import BrowserTab
from pages.demoqa import DemoQa


@pytest.mark.parametrize("pages", [Accordion, Alerts, DemoQa, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(4)
    assert page.head_viewport.exist()

    assert page.head_viewport.get_dom_attribute('name') =='viewport'


