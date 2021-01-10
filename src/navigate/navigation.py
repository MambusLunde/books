import selenium
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import Levenshtein.StringMatcher
from Levenshtein.StringMatcher import ratio

def amazon_driver():
    amazon = "https://www.amazon.com"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1420,1080')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--log-level=3')
    driver = webdriver.Chrome(options=chrome_options)
    
    driver.get(amazon) 

    return driver

def amazon_search(driver, search_term):   
    Select(driver.find_element_by_id("searchDropdownBox")).select_by_value("search-alias=stripbooks")
    
    driver.find_element_by_id("twotabsearchtextbox").send_keys(search_term)
    driver.find_element_by_id("nav-search-submit-button").click()

    return driver

## This will eventually be made fancier than just choose first result
def choose_result(driver, search_term):
    

    cand_list = []

    for index in range(0,21):
        try:
            title = driver.find_element_by_xpath(f"//div[@data-index='{str(index)}']//span[@class='a-size-medium a-color-base a-text-normal']").text
        except Exception:
            title = '.....................................'
        try:
            author = driver.find_element_by_xpath(f"//div[@data-index='{str(index)}']//a[@class='a-size-base a-link-normal']").text
        except Exception:
            try:
                author = driver.find_element_by_xpath(f"//div[@data-index='{str(index)}']//span[@class='a-size-base'][2]").text
            except Exception:
                author = '.....................................'
        
        title = title.split(':')[0]
        
        to_match = title + ' ' + author
        lev_ratio = ratio(str.lower(search_term), str.lower(to_match))
        cand_list.append(lev_ratio)

    most_likely = cand_list.index(max(cand_list))

    driver.find_element_by_xpath(f"//div[@data-index='{str(most_likely)}']//a[@class='a-link-normal a-text-normal']").click()

    return driver
