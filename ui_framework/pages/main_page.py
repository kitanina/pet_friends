from selenium.webdriver.common.by import By
from ui_framework.pages.base_page import BasePage


class MainPage(BasePage):
    """ Class for Main page. """
    @property
    def card_deck_grid(self):
        return self.driver.find_element(By.XPATH, '//div[@class="card-deck"]')
