import pytest
from Page_object import config
from Page_object.utils.driver_factory import driver_factory


@pytest.fixture(scope='function')
def driver(pytestconfig, request):
    browser = pytestconfig.getoption('browser')
    driver = driver_factory(browser)
    driver.maximize_window()
    url = request.node.get_closest_marker('url')
    if url and url.args:
        url = url.args[0]
    else:
        url = config.browser.base_url
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
