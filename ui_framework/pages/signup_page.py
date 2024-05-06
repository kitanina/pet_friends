from selenium.webdriver.common.by import By
from ui_framework.pages.base_page import BasePage


class SignUpPage(BasePage):
    @property
    def registration_button(self):
        return self.driver.find_element(By.XPATH, '//button[contains(@onclick,"document.location=")]')

    def get_new_user_page(self):
        self.registration_button.click()
        from new_user_page import NewUserPage
        return NewUserPage(self.driver)
