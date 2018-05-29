from src.utils import set_chrome

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import exceptions

driver = set_chrome("159.65.234.60:8080")
driver.get("https://katcr.co/")
search_bar = driver.find_element_by_id("contentSearch")
search_bar.send_keys("Patrick Melrose S01E03")
search_key = driver.find_element_by_id("searchTool").find_element_by_css_selector("button").click()


WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'text--error')))
reload_button = driver.find_element_by_class_name("text--error").find_element_by_css_selector('a').click()

