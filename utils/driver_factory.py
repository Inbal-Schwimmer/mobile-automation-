from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from utils.config import ANDROID_CONFIG,IOS_CONFIG

class DriverFactory:

    @staticmethod
    def create_driver(platform):
        if platform == "Android":
            options = UiAutomator2Options()
            options.platformName = ANDROID_CONFIG["platformName"]
            options.deviceName = ANDROID_CONFIG["deviceName"]
            options.app = ANDROID_CONFIG["app"]
            options.automationName = ANDROID_CONFIG["automationName"]  # Use the automationName from config
            options.appPackage = ANDROID_CONFIG["appPackage"]
            options.appActivity = ANDROID_CONFIG["appActivity"]
        elif platform == "iOS":
            options = XCUITestOptions()
            options.platformName = IOS_CONFIG["platformName"]
            options.deviceName = IOS_CONFIG["deviceName"]
            options.app = IOS_CONFIG["app"]  # example need to update
            options.automationName = IOS_CONFIG["automationName"]
            options.bundleId = IOS_CONFIG["bundleId"]
        else:
            raise ValueError(f"Unknown platform: {platform}")

        driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
        return driver
