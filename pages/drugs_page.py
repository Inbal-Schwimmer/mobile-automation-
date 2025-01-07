import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class DrugsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    MY_DRUGS_BTN = (AppiumBy.ACCESSIBILITY_ID, "profile_card_0")
    ADD_DRUGS_BTN = (AppiumBy.ACCESSIBILITY_ID, "Add Drugs")
    # SEARCH_DRUG_TF = (AppiumBy.ACCESSIBILITY_ID, "search_drug_name_tf'")
    ANDROID_SEARCH_DRUG_TF  = (AppiumBy.XPATH, "//android.widget.EditText")
    DOPICAR_DRUG = (AppiumBy.ACCESSIBILITY_ID, "Dopicar\nדופיקר")
    NEXT_BTN = (AppiumBy.ACCESSIBILITY_ID, "next")
    ADD_REMINDER_BTN = (AppiumBy.ACCESSIBILITY_ID, "add_notification")
    SAVE_REMINDER_BTN = (AppiumBy.ACCESSIBILITY_ID, "date_time_picker_save")
    DAILY_MEDICATION_FREQUENCY = (AppiumBy.ACCESSIBILITY_ID, "selection_0\nevery_day")
    DIALOG_NEXT_BTN = (AppiumBy.ACCESSIBILITY_ID, "my_drugs_add_drug_dialog_next")
    MY_DRUGS_TAB = (AppiumBy.ACCESSIBILITY_ID, "my_drugs_tab_drugs\nכרטיסייה 2 מתוך 2")
    DOSAGE_250_25 = (AppiumBy.ACCESSIBILITY_ID, "250MG/25MG")

    def search_drug(self, medication, platform):
        if platform == "Android":
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.ANDROID_SEARCH_DRUG_TF))
            element.click()
            time.sleep(2)
            element.clear()
            element.send_keys(medication)

    def add_drug(self, medication, platform):
        self.click(self.ADD_DRUGS_BTN)
        with allure.step("Search and add medication"):
            self.search_drug(medication, platform)
            self.click(self.DOPICAR_DRUG)
        with allure.step("Select dosage and frequency"):
            # select dosage by index
            self.click(self.DOSAGE_250_25)
            # self.click_selection_locator("1")
            self.click(self.NEXT_BTN)
            # select medication frequency
            self.click(self.DAILY_MEDICATION_FREQUENCY)
            self.click(self.NEXT_BTN)
        with allure.step("add reminder"):
            self.click(self.ADD_REMINDER_BTN)
            self.click(self.SAVE_REMINDER_BTN)
            self.click(self.NEXT_BTN)
            # add drug summary screen
            self.click(self.NEXT_BTN)
            self.click(self.DIALOG_NEXT_BTN)