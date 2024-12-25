import os

import allure
import pytest
from utils.driver_factory import DriverFactory


# Capture screenshot on test failure
def pytest_exception_interact(report):
    if report.failed:
        allure.attach(body=pytest.driver.get_screenshot_as_png(), name="screenshot",
                      attachment_type=allure.attachment_type.PNG)

@pytest.fixture
def setup_driver(platform):
# def setup_driver(request):
    # platform = request.param  # Get platform from test param
    driver = DriverFactory.create_driver(platform)  # Initialize driver based on the platform
    yield driver
    driver.quit()

# Session finish hook for allure report
def pytest_sessionfinish() -> None:
    environment_properties = {
        'browser': pytest.driver.name,
        'driver_version': pytest.driver.capabilities['browserVersion']
    }
    allure_env_path = os.path.join("allure-results", 'environment.properties')
    with open(allure_env_path, 'w') as f:
        data = '\n'.join([f'{variable}={value}' for variable, value in environment_properties.items()])
        f.write(data)