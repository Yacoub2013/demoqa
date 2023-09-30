
from pages.base_page import BasePage
from components.components import WebElement
from selenium.webdriver.common.by import By


class DemoQa(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)

        self.icona = WebElement(driver,'#app>header>a')
        self.elements = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')


        self.elements_1 = WebElement(driver, 'div >h5')


