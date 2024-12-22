
import pytest
from pages.login_page import LoginPage


class TestLogin:

    @pytest.mark.parametrize("platform", ["Android", "iOS"])  # Parametrize the platform
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
        login_page.click2(login_page.LOGIN_BUTTON)
        assert login_page.NO_EMAIL_ERROR_TEXT

    # @pytest.mark.parametrize("platform", ["Android", "iOS"])
    # def test_no_password_error(self, setup_driver, platform):
    #     driver = setup_driver
    #     login_page = LoginPage(driver)
    #     login_page.click_on_back_button(platform)
    #     login_page.click2(login_page.LOGIN_BUTTON)
    #     assert login_page.NO_PASSWORD_ERROR_TEXT


        # login_page.handle_permission_dialog("Android", "physical_activity")

        # Perform login
        # login_page.login("inbal.schwimmer@example.com", "123456")
        # TODO: Add proper assertions to verify login success
