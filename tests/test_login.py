import time
import allure
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage


class TestLogin:


    @pytest.mark.parametrize("platform", ["Android"])  # Parametrize the platform
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify that login fails without entering an email.")
    @allure.epic("Login Tests")
    # @pytest.mark.parametrize("platform", ["Android"])
    # @pytest.mark.parametrize("setup_driver", ["Android"], indirect=True)
    def test_no_mail_error(self, setup_driver, platform):
        driver = setup_driver
        login_page = LoginPage(driver)
        # Handle permission dialogs
        login_page.handle_permission_dialog(platform, "physical_activity")
        login_page.handle_permission_dialog(platform, "record_audio")
        login_page.handle_permission_dialog(platform, "send_notifications")
        login_page.click_on_back_button(platform)
        time.sleep(2)
        # login_page.enter_email("Inbal@remepy.com")
        login_page.enter_password("123456")
        login_page.click2(login_page.LOGIN_BUTTON)
        value = login_page.element_exist(login_page.NO_EMAIL_ERROR_TEXT)
        assert value == True


    @pytest.mark.parametrize("platform", ["Android"])
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify that login fails without entering an password.")
    @allure.epic("Login Tests")
    def test_no_password_error(self, setup_driver, platform):
        driver = setup_driver
        login_page = LoginPage(driver)
        login_page.click_on_back_button(platform)
        login_page.click2(login_page.LOGIN_BUTTON)
        assert login_page.NO_PASSWORD_ERROR_TEXT

    @pytest.mark.parametrize("platform", ["Android"])
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Verify success login when entering the correct credentials")
    @allure.epic("Login Tests")
    def test_success_login(self, setup_driver, platform):
        driver = setup_driver
        login_page = LoginPage(driver)
        home_page = HomePage(driver)
        login_page.handle_permission_dialog(platform, "physical_activity")
        login_page.handle_permission_dialog(platform, "record_audio")
        login_page.handle_permission_dialog(platform, "send_notifications")
        login_page.click_on_back_button(platform)
        time.sleep(2)
        login_page.enter_email("inbal.schwimmer@remepy.com")
        login_page.enter_password("123456")
        login_page.click2(login_page.LOGIN_BUTTON)
        value = home_page.element_exist(home_page.START_DAY_ACTIVITY_BTN)
        assert value == True
