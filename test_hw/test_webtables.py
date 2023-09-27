from pages.webtables import Webtables
from conftest import browser
import time


def test_webtables(browser):
    page = Webtables(browser)
    page.visit()
    browser.set_window_size(2000, 2000)
    page.btn_add.click()
    page.first_name.send_keys('Mustafa')
    page.last_name.send_keys('Yacoub')
    page.user_email.send_keys('mustafa@mail.ru')
    page.user_age.send_keys('38')
    page.salary.send_keys('200000')
    page.department.send_keys('miscellaneous')
    page.btn_submit.click_force()
    # time.sleep(5)

    page.pancil.click()
    page.first_name.clear()
    page.first_name.send_keys('NONONONONO')
    page.btn_submit.click_force()
    time.sleep(10)
    assert page.first_name_typ.get_text() == ('NONONONONO')

    if page.pancil.click():
        return page.form_reg
    else:
        print('Тест пройден успешно')
