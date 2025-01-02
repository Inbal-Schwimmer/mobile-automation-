import allure
import pytest

from pages.drugs_page import DrugsPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


@pytest.mark.usefixtures("perform_login")
class TestDrugs:

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify user can access profile screen.")
    @allure.epic("Profile Screen Tests")
    def test_enter_profile_screen(self,setup_driver, platform):
        user_profile = ProfilePage(setup_driver)
        user_drugs = DrugsPage(setup_driver)
        user_profile.click(user_profile.PROFILE_BTN)
        user_drugs.click(user_drugs.ADD_DRUGS_BTN)
        # user_profile.click(user_profile.SEARCH_DRUG_TF)
        user_drugs.search_drug("dop", platform)
        user_drugs.click(user_drugs.DOPICAR_DRUG)
        # select dosage by index
        user_drugs.click_selection_locator("1")
        user_drugs.click(user_drugs.NEXT_BTN)
        user_drugs.click(user_drugs.DAILY_MEDICATION_FREQUENCY)
        user_drugs.click(user_drugs.NEXT_BTN)
        user_drugs.click(user_drugs.ADD_REMINDER_BTN)
        user_drugs.click(user_drugs.SAVE_REMINDER_BTN)
        user_drugs.click(user_drugs.NEXT_BTN)
        assert True