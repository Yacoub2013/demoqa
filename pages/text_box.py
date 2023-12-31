from components.components import WebElement
from pages.base_page import BasePage


class TextBox(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/text-box"
        super().__init__(driver, self.base_url)

        self.full_name = WebElement(driver, '#userName')
        self.current_address = WebElement(driver, '#currentAddress')
        self.submit = WebElement(driver, '#submit')
        self.name_down = WebElement(driver, '#name')
        self.current_address_down = WebElement(driver, '#currentAddress')

