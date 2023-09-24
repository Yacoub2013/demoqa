from components.components import WebElement
from pages.base_page import BasePage



class ModalDialogs(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.widgest = WebElement(driver, '#app > div > div > div.row > div:nth-child(1) > div > div > div:nth-child(4) > span > div > div.header-text > span > svg > path')
        self.tool_icon = WebElement(driver, '#app > header')
        self.title = WebElement(driver, 'head > title')





