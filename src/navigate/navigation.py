import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select

def amazonSearch(search_term):
    
    amazon = "https://www.amazon.com"

    
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox") #This make Chromium reachable
    options.add_argument("--no-default-browser-check") #Overrides default choices
    options.add_argument("--no-first-run")
    options.add_argument("--disable-default-apps") 

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
