import unittest

from pspark.requests import RateRequest


class TestRateRequest(unittest.TestCase):
    def test_dict_conversation(self):
        dto = RateRequest(
            currency_from="USD",
            currency_to="BTC",
            nonce=1,
        )

        self.assertEqual(
            dto.as_dict(),
            {
                "currency_from": "USD",
                "currency_to": "BTC",
                "nonce": 1,
            },
        )
