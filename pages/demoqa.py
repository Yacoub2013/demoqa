from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException



class DemoQa(BasePage):

    def click_on_the_icona(self):
        self.find_element(locator='#app>header>a').click() #вызываем метод который мы создале в родителе


    def exist_icona(self):
        try:
            self.find_element(locator='#app>header>a') #вызываем метод который мы создале в родителе
        except NoSuchElementException:
            return False
        return True

