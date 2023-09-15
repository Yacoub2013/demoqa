from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


class ElementsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)

        self.text_please = WebElement(driver,'#app > div > div > div.home-body > div > div:nth-child(1)')
        self.text_elements = WebElement(driver, 'div.playgound-headr > div')



