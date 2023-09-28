from pages.form_page import FormPage
from conftest import browser
import time


def test_login_form_validate(browser):
    page = FormPage(browser)
    page.visit()
    browser.set_window_size(1500, 1500)
    # page.first_name.send_keys('tester')
    # time.sleep(2)
    # page.last_name.send_keys('testerovich')
    # time.sleep(2)
    # page.user_email.send_keys('testerovich@ttt.tt')
    # time.sleep(2)
    # page.gender_radio_1.click_force()
    # time.sleep(2)
    # page.user_number.send_keys(1233333333)
    # page.state.click()
    # time.sleep(3)
    # page.state_2.click_force()
    # time.sleep(2)
    # page.city.click()
    # time.sleep(3)
    # page.city_1.click_force()
    # time.sleep(3)

    # page.btn_submit.click_force()
    # time.sleep(10)

    assert page.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert page.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert page.user_email.get_dom_attribute('placeholder') == 'name@example.com'
    assert page.user_email.get_dom_attribute('pattern') == "^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$"

    if page.btn_submit.click_force():
        return page.submit_form
    else:
        print("Тест пройден успешно")


