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
    actions = ActionChains(driver)
    actions.move_to_element(home_page.alerts_button).perform()

    try:
        WebDriverWait(driver, 10).until(EC.visibility_of(home_page.alerts_button))
        driver.execute_script("arguments[0].scrollIntoView();", home_page.alerts_button)
        home_page.alerts_button.click()
    except TimeoutException:
        print("Element is not found")


def test_is_tools_qa_logo_clickable(driver):
    home_page = HomePage(driver)
    assert home_page.tools_qa_logo.is_displayed()


def test_click_tools_qa_logo(driver):
    home_page = HomePage(driver)
    # home_page.tools_qa_logo.click()

    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[@href='https://demoqa.com']")))

        home_page.tools_qa_logo.click()
    except NoSuchElementException as e:
        print(f"Element is not found: {e}")


@pytest.mark.url(config.browser.alerts_url)
def test_click_on_browser_windows_button(driver):
    alerts_page = AlertsPage(driver)
    assert alerts_page.browser_windows_button.click()


@pytest.mark.url(config.browser.alerts_url)
def test_click_on_new_tab_button(driver):
     alerts_page = AlertsPage(driver)
     assert alerts_page.new_tab_button.click()
