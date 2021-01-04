from selenium import webdriver
from selenium.webdriver.support.ui import Select


amazon = "https://www.amazon.com"

driver = webdriver.Chrome()

# Go to the amazon webpage
driver.get(amazon)

# Specify that we're searching for books
Select(driver.find_element_by_id("searchDropdownBox")).select_by_value("search-alias=stripbooks")

# Insert the title of the book in the searchfield
driver.find_element_by_id("twotabsearchtextbox").send_keys("Stiletto")

# Click the search button
driver.find_element_by_id("nav-search-submit-button").click()

# Click on the first search result
# I will make this smarter so that it can match Authors and Titles for when the title is different
driver.find_element_by_xpath("//a[@class='a-link-normal a-text-normal']").click()

