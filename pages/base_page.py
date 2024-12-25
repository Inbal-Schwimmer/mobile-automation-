import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from marshmallow.utils import set_value
from selenium.common import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        return self.driver.find_element(*locator)

    def element_exist(self, locator):
        try:
            time.sleep(1)
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def click2(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator))
        element.click()
        # time.sleep(3)
        # self.driver.find_element(*locator).click()

    def input_text(self, locator, text):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        element.click()
        element.send_keys(text)


