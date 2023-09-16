from pages.demoqa import DemoQa
from conftest import browser


def test_icon_exist(browser):

    demo_qa_page = DemoQa(browser)  # создаем страницу с которой мы будем работать
    demo_qa_page.visit()  # вызываем везит к сайту (входим на сайт)
    demo_qa_page.icona.click()
    assert demo_qa_page.icona.exist()  # проверка
    assert demo_qa_page.equal_url()  # проверка










