import pytest
from Page_object import config
from Page_object.utils.driver_factory import driver_factory


@pytest.fixture(scope='function')
def driver(pytestconfig, request):
    browser = pytestconfig.getoption('browser')
    driver = driver_factory(browser)
    driver.maximize_window()
    url = config.browser.base_url if not request.node.get_closest_marker('url').args[0] else \
    request.node.get_closest_marker('url').args[0] # это можно порефакторить но для наглядности думаю должно быть понятно
    driver.get(url)
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        action='store',
        default='chrome',
        help='Help information'
    )
