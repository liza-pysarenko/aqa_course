import pytest
from Page_object import config
from Page_object.utils.driver_factory import driver_factory


@pytest.fixture(scope='function')
def driver(pytestconfig):
    browser = pytestconfig.getoption('browser')
    driver = driver_factory(browser)
    driver.maximize_window()
    driver.get(config.browser.base_url)
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        action='store',
        default='chrome',
        help='Help information'
    )
