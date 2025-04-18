import unittest

from pspark.requests import TransactionRequest


class TestTransactionRequest(unittest.TestCase):
    def test_dict_conversation(self):
        dto = TransactionRequest(
            wallet_id="79CDA5A3-C688-4996-8D20-3EDDF4E6B70B",
            reference="uuid",
            nonce=1,
        )

        self.assertEqual(
            dto.as_dict(),
            {
                "reference": "uuid",
                "nonce": 1,
            },
        )
        self.assertEqual("79CDA5A3-C688-4996-8D20-3EDDF4E6B70B", dto.wallet_id)
