import selenium
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://google.com")

search_input = driver.find_element_by_name("q").send_keys("test_selenuim")
search_button = driver.find_element_by_name("btnK").click()
driver.save_screenshot("screenshot.png")
