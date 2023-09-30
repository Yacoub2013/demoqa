from components.components import WebElement
from pages.base_page import BasePage


class ModalDialogs(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.widgest = WebElement(driver,
                                  '#app > div > div > div.row > div:nth-child(1) > div > div > div:nth-child(4) > span > div > div.header-text > span > svg > path')
        self.tool_icon = WebElement(driver, '#app > header')

        self.small_modal = WebElement(driver, '#showSmallModal')
        self.large_modal = WebElement(driver, '#showLargeModal')
        self.small_modal_close = WebElement(driver, '#closeSmallModal')
        self.large_modal_close = WebElement(driver, '#closeLargeModal')
