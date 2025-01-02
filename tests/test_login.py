import time
import allure
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.skip_login
class TestLogin:

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify that login fails without entering an email.")
    @allure.epic("Login Tests")
    def test_no_mail_error(self, setup_driver, platform):
        # driver = setup_driver
        login_page = LoginPage(setup_driver)
        login_page.open_app_after_installation("", "123456", platform)
        error_exist = login_page.element_exist(login_page.NO_EMAIL_ERROR_TEXT)
        assert error_exist == True

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify that login fails without entering an password.")
    @allure.epic("Login Tests")
    def test_no_password_error(self, setup_driver, platform):
        # driver = setup_driver
        login_page = LoginPage(setup_driver)
        login_page.open_app_after_installation("automation@remepy.com", "", platform)
        error_exist = login_page.element_exist(login_page.NO_PASSWORD_ERROR_TEXT)
        assert error_exist == True

    @pytest.mark.usefixtures("post_test_cleanup")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Verify success login when entering the correct credentials")
    @allure.epic("Login Tests")
    def test_success_login(self, setup_driver, platform):
        # driver = setup_driver
        login_page = LoginPage(setup_driver)
        home_page = HomePage(setup_driver)
        login_page.open_app_after_installation("esan@remepy.com", "123456", platform)

        value = home_page.element_exist(home_page.START_DAY_ACTIVITY_BTN)
        assert value == True
