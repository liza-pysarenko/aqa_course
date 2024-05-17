from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver):
        self.__driver = driver

    @property
    def driver(self):
        return self.__driver

    def wait_until(self, locator, condition, timeout=10) -> WebElement:
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(condition(locator))

    def wait_until_not(self, locator, condition, timeout=10) -> WebElement:
        wait = WebDriverWait(self.driver, timeout)
        return wait.until_not(condition(locator))

    def click_element(self, locator):
        condition = EC.element_to_be_clickable
        element = self.wait_until(locator, condition)
        element.click()

    def is_element_clickable(self, locator):
        condition = EC.element_to_be_clickable
        return self.wait_until(locator, condition)

    def scroll_into_view(self, element: WebElement):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def find_element(self, by, locator):
        return self.driver.find_element(by, locator)

    def get_text(self, locator):
        condition = EC.visibility_of_element_located
        element = self.wait_until(locator, condition)
        return element.text
