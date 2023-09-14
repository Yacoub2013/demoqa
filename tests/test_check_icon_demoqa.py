from pages.demoqa import DemoQa
from conftest import browser


def test(browser):

    demo_qa_page = DemoQa(browser)  # создаем страницу с которой мы будем работать
    demo_qa_page.visit() # вызываем везит к сайту (входим на сайт)
    demo_qa_page.click_on_the_icona()
    assert demo_qa_page.exist_icona() # проверка
    assert demo_qa_page.equale_url()  # проверка









