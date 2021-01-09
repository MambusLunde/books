import selenium
import re

def truncate_url(url):
    base = 'https://www.amazon.com'

    pattern = r'/dp/\d+'

    try: 
        productNumber = re.findall(pattern, url)[0]
    except Exception:
        productNumber = ''

    shortURL = base + productNumber

    return shortURL

def extract_title(driver): 
    titles = driver.find_element_by_id("productTitle").text
    try:
        split_title = titles.split(':')
        title = split_title[0] 
        subtitle = split_title[1].strip()
    except Exception:
        title = titles
        subtitle = ''
    return title, subtitle

def extract_author(driver):
    try:
        author = driver.find_element_by_xpath("//a[@class='a-link-normal contributorNameID']").text
    except Exception:
        author = driver.find_element_by_xpath("//span[@class='author notFaded']//a[@class='a-link-normal']").text
    return author


def extract_image(driver):
    try:
        image = driver.find_element_by_xpath('//div[@id="main-image-container"]//img').get_attribute('src')
    except Exception:
        image = driver.find_element_by_id("main-image").get_attribute('src')

    return image
    

#def extract_blurb(driver):
