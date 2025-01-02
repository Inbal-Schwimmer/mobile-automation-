import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class DrugsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    MY_DRUGS_BTN = (AppiumBy.ACCESSIBILITY_ID, "profile_card_0")
    ADD_DRUGS_BTN = (AppiumBy.ACCESSIBILITY_ID, "profile_card_1")
    SEARCH_DRUG_TF = (AppiumBy.ACCESSIBILITY_ID, "search_drug_name_tf'")
    ANDROID_SEARCH_DRUG_TF = (AppiumBy.XPATH, "//android.widget.EditText")
    DOPICAR_DRUG = (AppiumBy.ACCESSIBILITY_ID, "Dopicar\nדופיקר")
    NEXT_BTN = (AppiumBy.ACCESSIBILITY_ID, "next_button")
    ADD_REMINDER_BTN = (AppiumBy.ACCESSIBILITY_ID, "add_notification")
    SAVE_REMINDER_BTN = (AppiumBy.ACCESSIBILITY_ID, "date_time_picker_save")
    DAILY_MEDICATION_FREQUENCY = (AppiumBy.ACCESSIBILITY_ID, "selection_tile_0\nבכל יום")

    def search_drug(self, text, platform):
        if platform == "Android":
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.ANDROID_SEARCH_DRUG_TF))
            element.click()
            time.sleep(2)
            element.clear()
            element.send_keys(text)
