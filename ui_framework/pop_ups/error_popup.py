from selenium.webdriver.common.by import By
from base_popup import BasePopup


class ErrorPopup(BasePopup):
    locator = (By.XPATH, '//*[text() = "Error"]/../..')
