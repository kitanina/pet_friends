from selenium.webdriver.common.by import By
from ui_framework.pages.base_page import BasePage


class NewUserPage(BasePage):

    @property
    def name_input(self):
        return self.driver.find_element(By.XPATH, '//*[@id="name"]')

    @property
    def email_input(self):
        return self.driver.find_element(By.XPATH, '//*[@id="email"]')

    @property
    def password_input(self):
        return self.driver.find_element(By.XPATH, '//*[@id="pass"]')

    @property
    def registration_button(self):
        return self.driver.find_element(By.XPATH, '//button[@type="submit"]')

    @property
    def have_account(self):
        return self.driver.find_element(By.XPATH, '//a[@href="/login"]')

    @property
    def alert_message(self):
        return self.driver.find_element(By.XPATH, '//*[@role="alert"]')

    def set_name(self, name):
        self.name_input.send_keys(name)

    def set_email(self, email):
        self.email_input.send_keys(email)

    def set_password(self, password):
        self.password_input.send_keys(password)

    def get_user_page(self, name, email, password):
        self.set_name(name)
        self.set_email(email)
        self.set_password(password)
        self.registration_button.click()
        from user_page import UserPage
        return UserPage(self.driver)

    def get_alert_message(self):
        self.registration_button.click()
        return self.alert_message.text


