from conftest import browser
from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_navigation(browser):
    demo_qa_page = DemoQa(browser)
    page = ElementsPage(browser)
    demo_qa_page.visit()
    demo_qa_page.btn_element.click()

    page.btn_sidebar_first.click()
    demo_qa_page.refresh()
            # Додоелать дома







