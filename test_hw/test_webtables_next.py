from pages.webtables import Webtables
from conftest import browser
import time


def test_webtables_next(browser):
    page = Webtables(browser)
    page.visit()
    #browser.set_window_size(2000, 2000)
    page.rows.click()
    # time.sleep(10)
    page.rows_5.click()
    # time.sleep(10)
    assert not page.page_next.click()
    assert not page.page_previos.click()

    page.btn_add.click()
    page.first_name.send_keys('Mustafa')
    page.last_name.send_keys('Yacoub')
    page.user_email.send_keys('mustafa@mail.ru')
    page.user_age.send_keys('38')
    page.salary.send_keys('200000')
    page.department.send_keys('miscellaneous')
    page.btn_submit.click_force()
    # time.sleep(5)

    page.btn_add.click()
    page.first_name.send_keys('Mustafa')
    page.last_name.send_keys('Yacoub')
    page.user_email.send_keys('mustafa@mail.ru')
    page.user_age.send_keys('38')
    page.salary.send_keys('200000')
    page.department.send_keys('miscellaneous')
    page.btn_submit.click_force()
    # time.sleep(5)

    page.btn_add.click()
    page.first_name.send_keys('Mustafa')
    page.last_name.send_keys('Yacoub')
    page.user_email.send_keys('mustafa@mail.ru')
    page.user_age.send_keys('38')
    page.salary.send_keys('200000')
    page.department.send_keys('miscellaneous')
    page.btn_submit.click_force()
    #time.sleep(5)


    page.page_next.click()
    #time.sleep(5)
    assert page.page_rows.get_dom_attribute('value') == '2'
    page.page_previos.click()
    assert page.page_rows.get_dom_attribute('value') == '1'
    #time.sleep(5)