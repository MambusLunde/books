import pytest

from scraping.extraction import truncate_url, extract_title, extract_author, extract_image
from navigate.navigation import amazon_search, choose_result

class TestTruncateURL(object):
    def test_working_url(self):
        test_url = "https://www.amazon.com/4-Hour-Workweek-Escape-Live-Anywhere/dp/0307465357/ref=sr_1_2?crid=2ZLOL1W9X6TPR&dchild=1&keywords=the+4+hour+work+week&qid=1608444375&s=books&sprefix=the+4hou%2Cstripbooks%2C209&sr=1-2"
        actual = truncate_url(test_url)
        expected = 'https://www.amazon.com/dp/0307465357'
        assert actual == expected, f"Expected: {expected}, Actual: {actual}"

    def test_wrong_url(self):
        test_url = 'https://www.facebook.com'
        actual = truncate_url(test_url)
        expected ="https://www.amazon.com"
        assert actual == expected, f"Expected: {expected}, Actual: {actual}"

class TestExtractTitle(object):
    def test_DataLoom(self):
        search_term = "The Data Loom"
        expected_title = "The Data Loom"
        expected_subtitle = "Weaving Understanding by Thinking Critically and Scientifically with Data"
        actual_title, actual_subtitle = extract_title(choose_result(amazon_search(search_term),search_term))
        assert actual_title == expected_title, f"Expected: {expected_title}, Actual: {actual_title}"
        assert actual_subtitle == expected_subtitle, f"Expected: {expected_subtitle}, Actual: {actual_subtitle}"

    def test_RhythmOfWar(self):
        search_term = "Rhythm of War"
        expected_title = search_term
        expected_subtitle = 'The Stormlight Archive, Book 4'
        actual_title, actual_subtitle = extract_title(choose_result(amazon_search(search_term), search_term))
        assert actual_title == expected_title, f"Expected: {expected_title}, Actual: {actual_title}"
        assert actual_subtitle == expected_subtitle, f"Expected: {expected_subtitle}, Actual: {actual_subtitle}"

class TestExtractAuthor(object):
    def test_DataLoom(self):
        search_term = "The Data Loom"
        expected = "Stephen Few"
        actual = extract_author(choose_result(amazon_search(search_term), search_term))
        assert actual == expected, f"Expected: {expected}, Actual: {actual}"


    def test_RhythmOfWar(self):
        search_term = "Rhythm of War"
        expected = "Brandon Sanderson"
        actual = extract_author(choose_result(amazon_search(search_term), search_term))
        assert actual == expected, f"Expected: {expected}, Actual: {actual}"

class TestExtractImage(object):
    def test_DataLoom(self):
        search_term = "The Data Loom"
        expected = "https://images-na.ssl-images-amazon.com/images/I/41gHdOK6zPL._SX331_BO1,204,203,200_.jpg"
        actual = extract_image(choose_result(amazon_search(search_term), search_term))
        assert actual == expected, f"Expected: {expected}, Actual: {actual}"

    def test_RhythmOfWar(self):
        search_term = "Rhythm of War"
        expected = "https://m.media-amazon.com/images/I/61kddyNOd5L.jpg"
        actual = extract_image(choose_result(amazon_search(search_term), search_term))
        assert actual == expected, f"Expected: {expected}, Actual: {actual}"
