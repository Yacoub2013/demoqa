from selenium.webdriver.common.by import By

from components.components import WebElement
from pages.base_page import BasePage


class Webtables(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/webtables"
        super().__init__(driver, self.base_url)

        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.user_age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')
        self.btn_submit = WebElement(driver, '#submit')
        self.pancil = WebElement(driver, '#edit-record-4 > svg')
        self.first_name_typ = WebElement(driver,'#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(1)')
        self.form_reg = WebElement(driver, '#registration-form-modal')
        self.delite_4 = WebElement(driver, '#delete-record-4 > svg > path')
        self.delite_1 = WebElement(driver, '#edit-record-1')
        self.delite_2 = WebElement(driver, '#delete-record-2 > svg > path')
        self.delite_3 = WebElement(driver, '#delete-record-3 > svg > path')
        self.no_rows_found = WebElement(driver, 'div.rt-noData')
        self.rows =WebElement(driver,'#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.select-wrap.-pageSizeOptions > select' )
        self.rows_5 = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.select-wrap.-pageSizeOptions > select > option:nth-child(1)')
        self.page_rows =WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.-pageInfo > div > input[type=number]')
        self.page_next = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-next > button')
        self.page_previos = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-previous > button')
        self.first_line = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(1) > div > div:nth-child(1)')
        self.btn_fn = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div:nth-child(1) > div.rt-resizable-header-content')