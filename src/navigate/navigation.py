import selenium
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def amazonSearch(search_term):
    
    amazon = "https://www.amazon.com"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1420,1080')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    
    driver.get(amazon)

    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, "searchDropdownBox")))
    

    Select(driver.find_element_by_id("searchDropdownBox")).select_by_value("search-alias=stripbooks")
    
    driver.find_element_by_id("twotabsearchtextbox").send_keys(search_term)
    driver.find_element_by_id("nav-search-submit-button").click()

    return driver

## This will eventually be made fancier than just choose first result
def chooseResult(driver, search_term):
    driver.find_element_by_xpath("//a[@class='a-link-normal a-text-normal']").click()

    return driver
