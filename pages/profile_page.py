import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from appium_flutter_finder.flutter_finder import FlutterElement, FlutterFinder


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    PROFILE_BTN = (AppiumBy.ACCESSIBILITY_ID, "profileIcon")





