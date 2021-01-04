from selenium import webdriver
from selenium.webdriver.support.ui import Select


amazon = "https://www.amazon.com"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(chrome_options=chrome_options)

# Go to the amazon webpage
driver.get(amazon)

# Specify that we're searching for books
Select(driver.find_element_by_id("searchDropdownBox")).select_by_visible_text("Books")

# Insert the title of the book in the searchfield
driver.find_element_by_id("twotabsearchtextbox").send_keys("Stiletto")

# Click the search button
driver.find_element_by_id("nav-search-submit-button").click()

# Click on the first search result
# I will make this smarter so that it can match Authors and Titles for when the title is different
driver.find_element_by_xpath("//a[@class='a-link-normal a-text-normal']").click()

