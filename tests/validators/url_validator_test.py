import unittest

from pspark.validators import validate_url


class TestUrlValidator(unittest.TestCase):
    def test_none_url(self):
        try:
            validate_url(None)
        except Exception as e:
            self.fail(f"validate_url(None) raised {e} unexpectedly!")

    def test_valid_urls(self):
        valid_urls = [
            "http://example.com",
            "https://example.com/path?query=string",
            "https://sub.domain.com",
        ]

        for url in valid_urls:
            try:
                validate_url(url)
            except ValueError as e:
                self.fail(f"validate_url({url}) raised {e} unexpectedly!")

    def test_invalid_urls(self):
        invalid_urls = [
            "example.com",
            "http://",
            "://example.com",
            "",
            "http:/example.com",
        ]
        for url in invalid_urls:
            with self.assertRaises(ValueError, msg=f"url: {url}"):
                validate_url(url)
