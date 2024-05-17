from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from Page_object.BasePage import BasePage
from Page_object.AlertsPage import AlertsPage


class HomePage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.alerts_button = self.find_element(By.XPATH, '//h5[contains(text(), "Alerts, Frame & Windows")]')
        self.tools_qa_logo = self.find_element(By.XPATH, "//a[@href='https://demoqa.com']")

    def find_alerts_button(self):
        self.find_element(self.alerts_button)

    def click_on_alerts_button(self):
        self.click_element(self.alerts_button)
        return AlertsPage(self.driver)

    def is_tools_qa_logo_clickable(self):
        self.is_element_clickable(self.tools_qa_logo)

    def click_on_tools_qa_logo(self):
        self.click_element(self.tools_qa_logo)
        return HomePage(self.driver)
