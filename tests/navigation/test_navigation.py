import pytest

from navigate.navigation import amazon_search, choose_result
from scraping.extraction import truncate_url

class TestAmazonSearch(object):
    def test_working_url(self):
        search_term = "The Data Loom"
        driver = amazon_search(search_term)
        expected_url = "https://www.amazon.com/s?k=The+Data+Loom&i=stripbooks&ref=nb_sb_noss" 
        actual_url = driver.current_url
        assert actual_url == expected_url, f"Expected: {expected_url}, Actual {actual_url}"

class TestChooseResult(object):
    def test_the_data_loom(self):
        search_term = "The Data Loom"
        url = choose_result(amazon_search(search_term), search_term).current_url
        expected_url = "https://www.amazon.com/dp/1938377117" 
        actual_url = truncate_url(url)
        assert actual_url == expected_url, f"Expected: {expected_url}, Actual {actual_url}"
