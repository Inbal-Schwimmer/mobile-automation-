from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions


class DriverFactory:

    @staticmethod
    def create_driver(platform):
        if platform == "Android":
            options = UiAutomator2Options()
            options.platformName = "Android"
            options.deviceName = "emulator-5554"
            options.app = "/Users/inbalschwimmershafir/Documents/GitHub/app-base-debug.apk"  # APK path
            # options.automationName = "UiAutomator2"  # Automation engine
            options.automationName = "Flutter"
            options.appPackage = "com.remepy.devbct"
            options.appActivity = "com.remepy.remepy.MainActivity"
        elif platform == "iOS":
            options = XCUITestOptions()
            options.platformName = "iOS"
            options.deviceName = "iPhone15"  # example need to update
            options.app = "/Users/inbalschwimmershafir/Documents/GitHub/Runner.app"  # example need to update
            options.automationName = "Flutter"
            # options.automationName = "XCUITest"
            options.bundleId = "com.remepy.devbct"  # example need to update
        else:
            raise ValueError(f"Unknown platform: {platform}")

        driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
        return driver
