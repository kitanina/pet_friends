from selenium.webdriver.common.by import By
from ui_framework.pages.base_page import BasePage


class UserPage(BasePage):
    """ Class for Main page. """
    @property
    def card_deck_grid(self):
        return self.driver.find_element(By.XPATH, '//div[@class="card-deck"]')

    @property
    def header_title(self):
        return self.driver.find_element(By.XPATH, '//a[@class="navbar-brand header2"]')

    @property
    def menu_button(self):
        return self.driver.find_element(By.XPATH, '//button[@class="navbar-toggler"]')

    @property
    def exit_button(self):
        return self.driver.find_element(By.XPATH, '//button[@class="btn btn-outline-secondary"]')

    @property
    def h1_header_title(self):
        return self.driver.find_element(By.XPATH, '//h1[@class="text-center"]')

    def get_sign_up_page(self):
        self.exit_button.click()
        from ui_framework.pages.signup_page import SignUpPage
        return SignUpPage(self.driver)


