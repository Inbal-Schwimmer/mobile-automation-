
import pytest
from pages.login_page import LoginPage


class TestLogin:

    # @pytest.mark.parametrize("platform", ["Android", "iOS"])  # Parametrize the platform
    @pytest.mark.parametrize("setup_driver", ["Android"], indirect=True)
    def test_login(self, setup_driver):
        driver = setup_driver
        login_page = LoginPage(driver)

        # Handle permission dialogs
        login_page.handle_permission_dialog("Android", "physical_activity")
        login_page.handle_permission_dialog("Android", "record_audio")
        login_page.handle_permission_dialog("Android", "send_notifications")

        # Perform login
        login_page.login("inbal.schwimmer@example.com", "123456")
        # TODO: Add proper assertions to verify login success
