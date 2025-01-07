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
    def test_add_drug(self,setup_driver, platform):
        user_profile = ProfilePage(setup_driver)
        user_drugs = DrugsPage(setup_driver)
        user_profile.click(user_profile.PROFILE_BTN)
        medication = "dop"
        user_drugs.add_drug(medication, platform)
        with allure.step("Verify drug was added to the user drug list"):
            user_drugs.click(user_drugs.MY_DRUGS_TAB)
            assert user_drugs.DOPICAR_DRUG

    def test_saved_drug_frequency(self,setup_driver,platform):
        user_profile = ProfilePage(setup_driver)
        user_drugs = DrugsPage(setup_driver)
        user_profile.click(user_profile.PROFILE_BTN)
        medication = "dop"
        user_drugs.add_drug(medication, platform)