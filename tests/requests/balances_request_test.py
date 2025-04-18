import unittest

from pspark.requests import BalancesRequest


class TestBalancesRequest(unittest.TestCase):
    def test_dict_conversation(self):
        dto = BalancesRequest(
            nonce=1,
        )

        self.assertEqual(
            dto.as_dict(),
            {
                "nonce": 1,
            },
        )
