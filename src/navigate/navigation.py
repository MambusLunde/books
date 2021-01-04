from selenium import webdriver
from selenium.webdriver.support.ui import Select

def amazonSearch(search_term):
    
    amazon = "https://www.amazon.com"

    driver = webdriver.Chrome()
    
    driver.get(amazon)
    
    Select(driver.find_element_by_id("searchDropdownBox")).select_by_visible_text("Books")
    
    driver.find_element_by_id("twotabsearchtextbox").send_keys(search_term)
    driver.find_element_by_id("nav-search-submit-button").click()

    return driver

## This will eventually be made fancier than just choose first result
def chooseResult(driver, search_term):
    driver.find_element_by_xpath("//a[@class='a-link-normal a-text-normal']").click()

    return driver
