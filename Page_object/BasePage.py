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
        element = self.scroll_into_view(locator)
        self.wait_until(element, EC.element_to_be_clickable)
        element.click()

    def is_element_clickable(self, locator):
        condition = EC.element_to_be_clickable
        return self.wait_until(locator, condition)

    def scroll_into_view(self, locator: tuple):
        element = self.wait_until(locator, EC.presence_of_element_located)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def is_element_visible(self, locator):
        condition = EC.visibility_of_element_located
        return self.wait_until(locator, condition)

    def browser_has_tabs_count(self, count: int):
        assert len(self.driver.window_handles) == count

    def switch_to_new_window(self):
        self.driver.switch_to.new_window()
        self.driver.switch_to.default_content()
