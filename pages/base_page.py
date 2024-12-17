
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator: tuple):
        return self.driver.find_element(*locator)

    def click(self, locator: tuple):
        self.find_element(locator).click()

    def input_text(self, locator: tuple, text: str):
        self.find_element(locator).send_keys(text)
