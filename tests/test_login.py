import json
import os
import allure
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from typing import Dict, List


def load_test_data() -> Dict[str, List[Dict[str, str]]]:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(base_dir, "data", "user_data.json")

    with open(json_file_path) as file:
        return json.load(file)

@pytest.mark.skip_login
class TestLogin:
    test_data = load_test_data()

    @pytest.mark.parametrize("data", [
        pytest.param(
            item,
            id=f"Invalid email test: {item['email']}"
        ) for item in load_test_data()["invalid_email"]
    ])
    @allure.severity(allure.severity_level.NORMAL)
    @allure.epic("Login Tests")
    @allure.story("Invalid Email Login Tests")
    def test_invalid_email(self, setup_driver, platform, data: Dict[str, str]):

        login_page = LoginPage(setup_driver)
        login_page.login_permissions(platform)

        with allure.step(f"Entering email: {data['email']}"):
            login_page.enter_email(data['email'])

        with allure.step("Entering password"):
            login_page.enter_password(data['password'])

        with allure.step("Clicking login button"):
            login_page.click(login_page.LOGIN_BUTTON)

        with allure.step("Checking for invalid email error message"):
            error_exist = login_page.element_exist(login_page.INVALID_EMAIL_TEXT)
            assert error_exist, f"Expected error message not displayed for email: {data['email']}"


    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify that login fails without entering an email.")
    @allure.epic("Login Tests")
    def test_no_mail_error(self, setup_driver, platform):
        login_page = LoginPage(setup_driver)
        login_page.open_app_after_installation("", "123456", platform)
        error_exist = login_page.element_exist(login_page.NO_EMAIL_ERROR_TEXT)
        assert error_exist == True

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify that login fails without entering an password.")
    @allure.epic("Login Tests")
    def test_no_password_error(self, setup_driver, platform):
        login_page = LoginPage(setup_driver)
        login_page.open_app_after_installation("automation@remepy.com", "", platform)
        error_exist = login_page.element_exist(login_page.NO_PASSWORD_ERROR_TEXT)
        assert error_exist == True

    @pytest.mark.parametrize("data", [
        pytest.param(
            item,
            id=f"Invalid email test: {item['email']}"
        ) for item in load_test_data()["valid_credentials"]
    ])
    @pytest.mark.usefixtures("post_test_cleanup")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Verify success login when entering the correct credentials")
    @allure.epic("Login Tests")
    def test_success_login(self, setup_driver, platform, data: Dict[str, str]):
        login_page = LoginPage(setup_driver)
        home_page = HomePage(setup_driver)
        valid_email = data['email']
        valid_password = data['password']

        login_page.open_app_after_installation(valid_email, valid_password , platform)

        value = home_page.element_exist(home_page.START_DAY_ACTIVITY_BTN)
        assert value == True