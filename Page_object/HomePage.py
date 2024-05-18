from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from Page_object.BasePage import BasePage
from Page_object.AlertsPage import AlertsPage
from Page_object.utils.by import by


class HomePage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.alerts_button = by('//h5[contains(text(), "Alerts, Frame & Windows")]')
        self.tools_qa_logo = by("//a[@href='https://demoqa.com']")

    def alert_btn_is_visible(self):
        return self.is_element_visible(self.alerts_button)

    def click_on_alerts_button(self):
        self.click_element(self.alerts_button)
        return AlertsPage(self.driver)

    def is_tools_qa_logo_visible_and_clickable(self):
        self.is_element_visible(self.tools_qa_logo)
        self.is_element_clickable(self.tools_qa_logo)

    def click_on_tools_qa_logo(self):
        self.click_element(self.tools_qa_logo)
        return HomePage(self.driver)
