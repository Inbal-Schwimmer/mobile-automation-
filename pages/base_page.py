import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator: tuple):
        return self.driver.find_element(*locator)

    def click(self, locator: tuple):
        self.find_element(locator).click()

    def click2(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator))
        element.click()
        # time.sleep(3)
        # self.driver.find_element(*locator).click()


    def input_text(self, locator: tuple, text: str):
        self.find_element(locator).send_keys(text)


