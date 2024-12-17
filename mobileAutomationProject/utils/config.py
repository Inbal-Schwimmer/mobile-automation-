CONFIG = {
    "android": {
        "platformName": "Android",
        "platformVersion": "15.0",
        "deviceName": "emulator-5554",
        "automationName": "UiAutomator2",
        "appPackage": "com.remepy.devbct",
        "appActivity": "com.remepy.remepy.MainActivity",
        "app": "/Users/inbalschwimmershafir/projects/universal.apk"
    },
    "ios": {
        "platformName": "iOS",
        "platformVersion": "14.0",
        "deviceName": "iPhone Simulator",
        "automationName": "XCUITest",
        "app": "/path/to/your/app.ipa",
        "udid": "your_device_udid",  # Modify with your device UDID
        "bundleId": "com.remepy.iosapp"  # Modify with your iOS app's bundle ID
    }
}
