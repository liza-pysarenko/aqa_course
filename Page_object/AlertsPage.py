from selenium.webdriver.chrome.webdriver import WebDriver
from Page_object.utils.by import by
from selenium.webdriver.common.by import By
from Page_object.BasePage import BasePage


class AlertsPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.browser_windows_button = by('//span[text()="Browser Windows"]')
        self.new_tab_button = by("id=tabButton")

    def click_on_browser_windows_button(self):
        self.click_element(self.browser_windows_button)

    def click_on_new_tab_button(self):
        self.click_element(self.new_tab_button)
