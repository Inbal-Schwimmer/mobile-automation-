import pytest
from utils.driver_factory import DriverFactory

@pytest.fixture
def setup_driver(request):
    platform = request.param  # Get platform from test param
    driver = DriverFactory.create_driver(platform)  # Initialize driver based on the platform
    yield driver
    driver.quit()