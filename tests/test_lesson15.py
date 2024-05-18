import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from Page_object.HomePage import HomePage
from Page_object.AlertsPage import AlertsPage
from tests.conftest import driver
from Page_object import config
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


@pytest.mark.usefixtures("driver")
def test_find_alerts_button(driver):
    home_page = HomePage(driver)
    assert home_page.alerts_button.is_displayed()


def test_click_alerts_button(driver):
    home_page = HomePage(driver)
    alert_btn = home_page.alert_btn_is_visible()
    driver.execute_script("arguments[0].scrollIntoView();",
                          alert_btn)  # лучше скрол вынести в отдельный файл и его уже использовать в шагах типа клик он
    home_page.click_on_alerts_button()


def test_is_tools_qa_logo_clickable(driver):
    home_page = HomePage(driver)
    home_page.is_tools_qa_logo_visible_and_clickable()


def test_click_tools_qa_logo(driver):
    home_page = HomePage(driver)
    home_page.click_on_tools_qa_logo()


@pytest.mark.url(config.browser.alerts_url)  # ты никак не используешь эту марку, сделал в конфтесте как сделать
def test_click_on_browser_windows_button(driver):
    alerts_page = AlertsPage(driver)
    alerts_page.click_on_browser_windows_button()


@pytest.mark.url(config.browser.alerts_url)  # ты никак не используешь эту марку, сделал в конфтесте как сделать
def test_click_on_new_tab_button(driver):
    alerts_page = AlertsPage(driver)
    alerts_page.click_on_new_tab_button() # ту
