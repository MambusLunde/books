from selenium import webdriver
from selenium.webdriver.support.ui import Select

amazon = "https://www.amazon.com"

driver = webdriver.Chrome()

driver.get(amazon)

Select(driver.find_element_by_id("searchDropdownBox")).select_by_visible_text("Books")

driver.find_element_by_id("twotabsearchtextbox").send_keys("Stiletto")
driver.find_element_by_id("nav-search-submit-button").click()