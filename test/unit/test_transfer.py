# -*- coding: utf-8 -*-
import unittest

from yandex_checkout.domain.models.amount import Amount
from yandex_checkout.domain.models.currency import Currency
from yandex_checkout.domain.models.transfer import Transfer


class TestTransfer(unittest.TestCase):

    def test_receipt_cast(self):
        self.maxDiff = None
        transfer = Transfer()
        transfer.account_id = '79990000000'
        transfer.amount = Amount({
            "value": '100.01',
            "currency": Currency.RUB
        })

        self.assertEqual({
            'account_id': '79990000000',
            "amount": {
                "value": 100.01,
                "currency": Currency.RUB
            }
        }, dict(transfer))

        self.assertEqual('79990000000', transfer.account_id)

        self.assertEqual({"value": 100.01, "currency": Currency.RUB}, dict(transfer.amount))
        self.assertEqual(transfer.amount.value, 100.01)

        with self.assertRaises(TypeError):
            transfer.amount = 'invalid type'
