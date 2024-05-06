from selenium.webdriver.support import expected_conditions


class BasePopup:

    def __init__(self, locator):
        self.locator = locator

    def click(self):
        self.wait.until(expected_conditions.element_to_be_clickable(self.locator)).click()

    def find_element_by_text(self):
        return self.driver.find_element_by_xpath(f'//*[text() = "{self.text}"]')
