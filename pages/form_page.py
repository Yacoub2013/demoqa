from selenium.webdriver.common.by import By

from components.components import WebElement
from pages.base_page import BasePage


class FormPage(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/automation-practice-form"
        super().__init__(driver, self.base_url)


        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.gender_radio_1 = WebElement(driver, '#gender-radio-1')
        self.user_number = WebElement(driver, '#userNumber')
        self.btn_submit = WebElement(driver, '#submit')
        self.modal_dialog = WebElement(driver, 'body > div.fade.modal.show > div')
        self.btn_close_modal = WebElement(driver, '#closeLargeModal')
        self.hobbies = WebElement(driver, '#hobbiesWrapper > div.col-md-9.col-sm-12 > div:nth-child(1)')
        self.corrent_address = WebElement(driver, '#currentAddress')
        self.state = WebElement(driver, '#state > div > div.css-1hwfws3>div ')
        self.state_0 = WebElement(driver, 'react-select-3-option-0')
        self.state_1 = WebElement(driver, 'react-select-3-option-1')
        self.state_2 = WebElement(driver, 'react-select-3-option-2')
        






