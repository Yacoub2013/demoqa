from components.components import WebElement
from pages.base_page import BasePage


class ElementsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)

        self.text_please = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6')
        self.text_elements = WebElement(driver, 'div.playgound-header >div')
        self.icona = WebElement(driver, '#app > header > a > img')
        self.btn_sidebar_first = WebElement(driver, 'div:nth-child(1) > span >div')
        self.btn_siderbar_first_textbox = WebElement(driver, 'div:nth-child(1)>div>ul>#item-0>span')
        self.basement = WebElement(driver, '#app > footer > span')
        self.centre = WebElement(driver, 'div.col-12.mt-4.col-md-6')
        self.btn_siderbar_first_checkbox = WebElement(driver, 'div:nth-child(1) > div > ul > #item-1 > span')
        self.btn_siderbar_first_seo = WebElement(driver, 'head > title')
        self.btns_first_menu = WebElement(driver, 'div:nth-child(1) > div > ul > li')
        self.nav_bar = WebElement(driver, 'div > nav')
        self.block_menu = WebElement(driver, 'div.row > div:nth-child(1)')
