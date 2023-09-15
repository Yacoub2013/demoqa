from pages.base_page import BasePage
from components.components import WepElement


class DemoQa(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)

        self.icona = WepElement(driver,'#app>header>a')
        self.element_1 = WepElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')









