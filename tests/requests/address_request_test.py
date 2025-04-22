import unittest

from pspark.requests import AddressRequest


class TestAddressRequest(unittest.TestCase):
    def test_dict_conversation_for_full_filled_object(self):
        dto = AddressRequest(
            wallet_id="79CDA5A3-C688-4996-8D20-3EDDF4E6B70B",
            reference="uuid",
            title="title",
            description="description",
            time_limit=15,
            callback_url="http://example.com",
            nonce=1,
        )

        self.assertEqual(
            dto.as_dict(),
            {
                "reference": "uuid",
                "title": "title",
                "description": "description",
                "time_limit": 15,
                "callback_url": "http://example.com",
                "nonce": 1,
            },
        )
        self.assertEqual("79CDA5A3-C688-4996-8D20-3EDDF4E6B70B", dto.wallet_id)

    def test_dict_conversation_for_partially_filled_object(self):
        dto = AddressRequest(
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

    def test_callback_url_validation(self):
        with self.assertRaises(
            ValueError, msg="AddressRequest callback_url validation failed."
        ):
            AddressRequest(
                wallet_id="79CDA5A3-C688-4996-8D20-3EDDF4E6B70B",
                reference="uuid",
                callback_url="invalid_url",
                nonce=1,
            )
