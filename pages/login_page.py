from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "התחברות")  # example need to update
    EMAIL_TF = (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='email_tf']")
    PASSWORD_TF = (AppiumBy.XPATH,"//android.widget.EditText[@resource-id='password_tf']")
    ANDROID_ALLOW_BTN = ("id", "com.android.permissioncontroller:id/permission_allow_button")
    ANDROID_ALLOW_RECORD_AUDIO_BTN = ("id", "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
    IOS_ALLOW_BTN = (AppiumBy.ACCESSIBILITY_ID, "Allow")
    ANDROID_BACK_BTN = (AppiumBy.XPATH, "// android.widget.Button")
    NO_EMAIL_ERROR_TEXT = (AppiumBy.ACCESSIBILITY_ID, "יש להזין כתובת מייל")
    INVALID_EMAIL_TEXT = (AppiumBy.ACCESSIBILITY_ID, "כתובת מייל לא תקינה")
    NO_PASSWORD_ERROR_TEXT = (AppiumBy.ACCESSIBILITY_ID, "הסיסמה חייבת להכיל לפחות 6 תווים")
    NEW_EMAIL_TF = (AppiumBy.XPATH, "email_tf")
    REG_EMAIL_TF = (AppiumBy.XPATH, "//android.widget.EditText[contains(@hint,'email_address')]")
    REG_PASSWORD_TF = (AppiumBy.XPATH, "//android.widget.EditText[contains(@hint, 'password')]")
    EMAIL_TEXTFIELD_LOCATOR = (AppiumBy.ACCESSIBILITY_ID, "email_tf")

    def enter_password(self,password):
        self.input_text(self.REG_PASSWORD_TF,password)

    def enter_email(self,email):
        self.input_text(self.REG_EMAIL_TF, email)

    def open_app_after_installation(self, email, password, platform):
        self.handle_permission_dialog(platform, "physical_activity")
        self.handle_permission_dialog(platform, "record_audio")
        self.handle_permission_dialog(platform, "send_notifications")
        self.click_on_back_button(platform)
        self.enter_email(email)
        self.enter_password(password)
        self.click(self.LOGIN_BUTTON)


    def print_element_in_screen(self):
        elements = self.driver.find_elements(AppiumBy.XPATH, "//*")  # Select all elements
        for element in elements:
            print("Tag:", element.tag_name)
            print("Content-desc:", element.get_attribute("content-desc"))
            print("Resource-id:", element.get_attribute("resource-id"))
            print("Text:", element.text)
            print("---")


    def handle_permission_dialog(self, platform: str, permission_type: str):
        try:
            if platform == "Android":
                if permission_type == "physical_activity":
                    WebDriverWait(self.driver, 5).until(
                        EC.element_to_be_clickable(self.ANDROID_ALLOW_BTN)
                    ).click()
                elif permission_type == "record_audio":
                    WebDriverWait(self.driver, 5).until(
                        EC.element_to_be_clickable(self.ANDROID_ALLOW_RECORD_AUDIO_BTN)
                    ).click()
                elif permission_type == "send_notifications":
                    WebDriverWait(self.driver, 5).until(
                        EC.element_to_be_clickable(self.ANDROID_ALLOW_BTN)
                    ).click()
                else:
                    pass
                    # raise ValueError(f"Unsupported permission type: {permission_type}")

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
            print(f"Permission dialog not found for {platform} - {e}. Continuing test.")

    def login_permissions(self, platform):
        self.handle_permission_dialog(platform, "physical_activity")
        self.handle_permission_dialog(platform, "record_audio")
        self.handle_permission_dialog(platform, "send_notifications")
        self.click_on_back_button(platform)


