from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from components.components import WepElement
from selenium.webdriver.common.by import By


class DemoQa(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)

        self.icona = WepElement(driver,'#app>header>a')
        self.elements = WepElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')










