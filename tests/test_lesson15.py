import pytest
from Page_object.HomePage import HomePage
from Page_object.AlertsPage import AlertsPage
from tests.conftest import driver
from Page_object import config


@pytest.mark.usefixtures("driver")
def test_find_alerts_button(driver):
    home_page = HomePage(driver)
    home_page.alert_btn_is_visible()


def test_click_alerts_button(driver):
    home_page = HomePage(driver)
    home_page.click_on_alerts_button()


def test_is_tools_qa_logo_clickable(driver):
    home_page = HomePage(driver)
    home_page.is_tools_qa_logo_visible_and_clickable()


def test_click_tools_qa_logo(driver):
    home_page = HomePage(driver)
    home_page.click_on_tools_qa_logo()


@pytest.mark.url(config.browser.alerts_url)
def test_click_on_browser_windows_button(driver):
    alerts_page = AlertsPage(driver)
    alerts_page.click_on_browser_windows_button()


@pytest.mark.url(config.browser.alerts_url)
def test_click_on_new_tab_button(driver):
    alerts_page = AlertsPage(driver)
    alerts_page.click_on_browser_windows_button()
    alerts_page.click_on_new_tab_button()
    alerts_page.browser_has_tabs_count(count=2)
    alerts_page.switch_to_new_window()
