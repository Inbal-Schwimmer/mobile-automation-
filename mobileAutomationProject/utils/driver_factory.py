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
            options.app = "/Users/inbalschwimmershafir/projects/universal.apk"  # APK path
            options.automationName = "UiAutomator2"  # Automation engine
            options.appPackage = "com.remepy.devbct"
            options.appActivity = "com.remepy.remepy.MainActivity"
        elif platform == "iOS":
            options = XCUITestOptions()
            options.platformName = "iOS"
            options.deviceName = "iPhone Simulator"  # example need to update
            options.app = "/path/to/your/app.ipa"  # example need to update
            options.automationName = "XCUITest"  # example need to update
            options.bundleId = "com.remepy.iosapp"  # example need to update
        else:
            raise ValueError(f"Unknown platform: {platform}")

        driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
        return driver
