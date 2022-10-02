import unittest

from extractor import get_valid_urls


class TestExtractor(unittest.TestCase):
    def test_parse_no_input(self):
        """
        Test that it returns nothing if nothing is passed
        """

    def test_parse_single_url(self):
        """
        Test that it can parse a valid url and returning it
        """

        url_input = "http://google.com"
        url_list = get_valid_urls({url_input})
        self.assertIn(url_input, url_list)

    def test_parse_multiple_urls(self):
        """
        Test that it can parse multiple urls and return those valid
        """

        url_input = "http://google.com"
        url_bad_input = "admaxlawecfn "
        url_list = get_valid_urls({url_input, url_bad_input})
        self.assertIn(url_input, url_list)
        self.assertNotIn(url_bad_input, url_list)


if __name__ == '__main__':
    unittest.main()
