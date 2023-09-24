import time
from conftest import browser
from pages.form_page import FormPage


def test_icon_exist(browser):

    form_page = FormPage(browser)
    form_page.visit()
    browser.set_window_size(1500, 1500)

    assert not form_page.modal_dialog.exist()
    time.sleep(2)
    form_page.first_name.send_keys('tester')
    time.sleep(2)
    form_page.last_name.send_keys('testerovich')
    time.sleep(2)
    form_page.user_email.send_keys('testerovich@ttt.tt')
    time.sleep(2)
    form_page.gender_radio_1.click_force()
    time.sleep(2)
    form_page.user_number.send_keys(1233333333)
    time.sleep(2)
    form_page.btn_submit.click_force()

    assert form_page.modal_dialog.exist()
    form_page.btn_close_modal.click_force()
    time.sleep(2)
    form_page.hobbies.click_force()
    time.sleep(2)
    form_page.corrent_address.send_keys('fdgjdf dfg dfjhg dfg')

    form_page.state.click()
    time.sleep(3)
    form_page.state_2.click_force()
    time.sleep(2)
    form_page.city.click()
    time.sleep(3)
    form_page.city_1.click_force()
    time.sleep(3)













