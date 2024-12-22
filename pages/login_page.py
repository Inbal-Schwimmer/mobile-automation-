from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class LoginPage(BasePage):
    LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "התחברות")  # example need to update
    USERNAME_FIELD = ("id", "username_field")  # example need to update
    PASSWORD_FIELD = ("id", "password_field")  # example need to update
    ANDROID_ALLOW_BTN = ("id", "com.android.permissioncontroller:id/permission_allow_button")
    ANDROID_ALLOW_RECORD_AUDIO_BTN = ("id", "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
    IOS_ALLOW_BTN = (AppiumBy.ACCESSIBILITY_ID, "Allow")
    ANDROID_BACK_BTN = (AppiumBy.XPATH, "// android.widget.Button")
    NO_EMAIL_ERROR_TEXT = (AppiumBy.ACCESSIBILITY_ID, "יש להזין כתובת מייל")
    NO_PASSWORD_ERROR_TEXT = (AppiumBy.ACCESSIBILITY_ID, "הסיסמה חייבת להכיל לפחות 6 תווים")
    # LOGIN_BUTTON_LOCATOR = (by_value_key, 'login_button')

    def login(self, username: str, password: str):
        self.input_text(self.USERNAME_FIELD, username)
        self.input_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)

    def handle_permission_dialog(self, platform: str, permission_type: str):
        try:
            if platform == "Android":
                if permission_type == "physical_activity":
                    WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable(self.ANDROID_ALLOW_BTN)
                    ).click()
                elif permission_type == "record_audio":
                    WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable(self.ANDROID_ALLOW_RECORD_AUDIO_BTN)
                    ).click()
                elif permission_type == "send_notifications":
                    WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable(self.ANDROID_ALLOW_BTN)
                    ).click()
                else:
                    raise ValueError(f"Unsupported permission type: {permission_type}")

            elif platform == "iOS":
                if permission_type in ["physical_activity", "record_audio"]:
                    self.click(self.IOS_ALLOW_BTN)
                else:
                    raise ValueError(f"Unsupported permission type: {permission_type}")

            else:
                raise ValueError(f"Unsupported platform: {platform}")

        except Exception as e:
            print(f"Permission dialog handling failed for {platform} - {permission_type}: {e}")

    def click_on_back_button(self, platform: str):
        try:
            if platform == "Android":
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.ANDROID_BACK_BTN)).click()

            elif platform == "iOS":
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.ANDROID_BACK_BTN)).click()

        except Exception as e:
            print(f"Permission dialog handling failed for {platform} : {e}")


