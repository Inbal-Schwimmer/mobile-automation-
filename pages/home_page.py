from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    START_DAY_ACTIVITY_BTN = (AppiumBy.ACCESSIBILITY_ID, "לתחילת הפעילות היומית")

