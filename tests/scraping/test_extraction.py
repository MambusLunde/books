import pytest

from scraping.extraction import truncateURL

class TestTruncateURL(object):
    def test_working_url(self):
        test_url = "https://www.amazon.com/4-Hour-Workweek-Escape-Live-Anywhere/dp/0307465357/ref=sr_1_2?crid=2ZLOL1W9X6TPR&dchild=1&keywords=the+4+hour+work+week&qid=1608444375&s=books&sprefix=the+4hou%2Cstripbooks%2C209&sr=1-2"
        actual = truncateURL(test_url)
        expected = 'https://www.amazon.com/dp/0307465357'
        assert actual == expected, f"Expected: {expected}, Actual: {actual}"

    def test_wrong_url(self):
        test_url = 'https://www.amazon.com'
        actual = truncateURL(test_url)
        expected ="https://www.amazon.com"
        assert actual == expected, f"Expected: {expected}, Actual: {actual}"