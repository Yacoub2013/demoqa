

from components.components import WebElement
from pages.base_page import BasePage


class Slider(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/slider"
        super().__init__(driver, self.base_url)


        self.slider = WebElement(driver, '#sliderContainer > div.col-9 > span > input')
        self.table = WebElement(driver, '#sliderValue')
        self.inp = WebElement(driver, '#sliderContainer > div.col-9 > span > div')


