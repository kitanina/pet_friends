import time
from selenium.common import NoSuchElementException

from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def refresh(self):
        self.driver.refresh()
        time.sleep(4)

    def back(self):
        self.driver.back()

    def get_current_url(self):
        return self.driver.current_url

    def get_session_id(self):
        return self.driver.session_id

    def close_window(self):
        return self.driver.close()

    def open_new_tab(self):
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.find_element(locator).click()

    def input_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    def is_visible(self, locator):
        return self.find_element(locator).is_displayed()

    def is_element_present(self, locator):
        try:
            self.find_element(locator)
            return True
        except NoSuchElementException:
            return False

    def read_data_grid(self, locator):
        return self.find_element(locator).text
