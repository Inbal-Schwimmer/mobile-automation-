import os
import allure
import pytest
from pages.login_page import LoginPage
from utils.driver_factory import DriverFactory


# Capture screenshot on test failure
def pytest_exception_interact(report):
    if report.failed and hasattr(pytest, "driver"):
        allure.attach(
            body=pytest.driver.get_screenshot_as_png(),
            name="screenshot",
            attachment_type=allure.attachment_type.PNG,
        )


def pytest_addoption(parser):
    # adds a command-line option (--platform) to pytest.
    # example : pytest --platform=Android
    parser.addoption("--platform", action="store", default="Android", help="Choose the platform: Android or iOS")


@pytest.fixture(scope="class")
def platform(request):
    # retrieves the value of the --platform option provided
    # via the command line (or defaults to "Android")
    return request.config.getoption("--platform")


@pytest.fixture(scope="class", autouse=True)
def setup_driver(platform):
    # Create driver based on the platform (Android or iOS)
    driver = DriverFactory.create_driver(platform)  # Initialize globally driver based on the platform
    pytest.driver = driver
    yield driver
    driver.quit()


# Fixture for performing login, using the setup_driver fixture
@pytest.fixture(scope="class")
def perform_login(setup_driver, platform):
    driver = setup_driver
    login_page = LoginPage(driver)

    def login():
        # Perform login (email and password can be passed dynamically if needed)
        login_page.open_app_after_installation("esan@remepy.com", "123456", platform=platform)

    # Try to perform login before the first test runs
    try:
        login()
    except Exception as e:
        print(f"Initial login failed: {e}. Retrying...")
        login()  # Retry login if the first attempt fails

    yield  # Pass the driver to the tests

    # Optional cleanup after all tests
    # example, you could add logout logic here if needed


@pytest.fixture(scope="class")
def app_installation(request, setup_driver, platform):
    driver = setup_driver
    login_page = LoginPage(driver)

    # Check if login is required
    perform_login = not request.node.get_closest_marker("skip_login")

    def install_and_login():
        # Install the app
        if platform == "Android":
            setup_driver.install_app(
                "/Users/inbalschwimmershafir/Documents/GitHub/frontend/apps/users_app/build/app/outputs/flutter-apk/app-base-debug.apk")
        elif platform == "iOS":
            setup_driver.install_app("/Users/inbalschwimmershafir/Documents/GitHub/Runner.app")

        if perform_login:
            login_page.open_app_after_installation("esan@remepy.com", "123456", platform=platform)

    # Try to install and login
    try:
        install_and_login()
    except Exception as e:
        print(f"App installation or login failed: {e}. Retrying...")
        install_and_login()  # Retry if the first attempt fails

    yield driver


@pytest.fixture
def post_test_cleanup(setup_driver, platform):
    # No need to yield driver, you can directly use the `setup_driver` fixture
    yield  # This signifies that setup is complete, and teardown will be executed after the test

    # Remove app to reset the state after the test finishes
    if platform == "Android":
        print("Removing Android app")
        setup_driver.remove_app("com.remepy.devbct")
        print("Reinstalling Android app")
        setup_driver.install_app(
            "/Users/inbalschwimmershafir/Documents/GitHub/frontend/apps/users_app/build/app/outputs/flutter-apk/app-base-debug.apk")
    elif platform == "iOS":
        setup_driver.remove_app("com.remepy.devbct")
        setup_driver.install_app("/Users/inbalschwimmershafir/Documents/GitHub/Runner.app")
