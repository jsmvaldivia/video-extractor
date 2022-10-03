import unittest

from extractor import validate


class TestExtractor(unittest.TestCase):
    def test_parse_no_input(self):
        """
        Test that it raises an exception if no url is passed   
        """

        url_input = "123123das"
        self.assertRaises(Exception, lambda: validate(url_input))

    def test_parse_single_url(self):
        """
        Test that it can parse a valid url and returning it
        """

        url_input = "http://google.com"
        valid_url = validate(url_input)
        self.assertIn(url_input, valid_url)


if __name__ == '__main__':
    unittest.main()
