from pages.elements_page import ElementsPage
from pages.demoqa import DemoQa
from conftest import browser


def test_go_to_page_elements(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)

    demo_qa_page.visit()
    assert demo_qa_page.equal_url()

    demo_qa_page.element_1.click()
    assert elements_page.equal_url()



