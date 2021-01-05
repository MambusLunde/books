from selenium import webdriver
from selenium.webdriver.support.ui import Select
from Levenshtein.StringMatcher import ratio 


amazon = "https://www.amazon.com"

driver = webdriver.Chrome()

# Go to the amazon webpage
driver.get(amazon)

# Specify that we're searching for books
Select(driver.find_element_by_id("searchDropdownBox")).select_by_value("search-alias=stripbooks")

# Insert the title of the book in the searchfield
driver.find_element_by_id("twotabsearchtextbox").send_keys("The Data Loom")

# Click the search button
driver.find_element_by_id("nav-search-submit-button").click()

# Click on the first search result
# I will make this smarter so that it can match Authors and Titles for when the title is different
# driver.find_element_by_xpath("//div[@data-index='1']//a[@class='a-link-normal a-text-normal']").click()
title = driver.find_element_by_xpath("//div[@data-index='1']//span[@class='a-size-medium a-color-base a-text-normal']").text
author = driver.find_element_by_xpath("//div[@data-index='1']//a[@class='a-size-base a-link-normal']").text

cand_list = []

for index in range(0,21):
    title = driver.find_element_by_xpath(f"//div[@data-index='{str(index)}']//span[@class='a-size-medium a-color-base a-text-normal']").text
    
    try:
        author = driver.find_element_by_xpath(f"//div[@data-index='{str(index)}']//a[@class='a-size-base a-link-normal']").text
    except:
        author = driver.find_element_by_xpath(f"//div[@data-index='{str(index)}']//span[@class='a-size-base'][2]").text
    try:
        title = title.split(':')[0]
    except:
        pass
    to_match = title + ' ' + author
    
    print(index, title, author)
    lev_ratio = ratio(str.lower("The data loom"), str.lower(to_match))
    cand_list.append(lev_ratio)

most_likely = cand_list.index(max(cand_list))
driver.find_element_by_xpath(f"//div[@data-index='{str(most_likely)}']//a[@class='a-link-normal a-text-normal']").click()


print(cand_list)
