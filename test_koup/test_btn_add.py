import time
from conftest import browser
from pages.herokuapp import Herokuapp
from components.components import WebElement
from pages.herokuapp_add import HerokuappAdd


def test_icon_exist(browser):
    page_1 = HerokuappAdd(browser)
    page = Herokuapp(browser)
    page.visit()

    assert page.add_remove.get_text() == 'Add/Remove Elements'
    page.add_remove.click()
    assert page_1.equal_url()
    assert page_1.add_element.get_text() == 'Add Element'
    assert page_1.add_element.get_dom_attribute('onclick') == 'addElement()'

    for i in range(4):
        page_1.add_element.click()
    assert page_1.delete.check_count_elements(4) #4 раза нажали на кнопку

    for element in page_1.delete.find_elements(): # проверили все четыре кнопки
        assert element.text == "Delete"


    while page_1.delete.exist(): # нажимает кнопку delete пока она не изчеснет (используем уникальный локатор)
        page_1.delete.click()
    assert not page_1.delete.exist()

    # assert page_1.add_element.get_text() == 'Delete' - не правильно
