import unittest
from io import StringIO
import sys

from mirasol_lab8 import (
    CreditCardPayment,
    PayPalPayment,
    CryptoPayment,
    checkout
)

class TestCreditCardPayment(unittest.TestCase):
    def test_valid_credit_card(self):
        cc = CreditCardPayment("1111111111111111")
        self.assertTrue(cc.validate())

    def test_invalid_credit_card_length(self):
        cc = CreditCardPayment("123456")
        self.assertFalse(cc.validate())

    def test_invalid_credit_card_characters(self):
        cc = CreditCardPayment("1111abcd1111abcd")
        self.assertFalse(cc.validate())

    def test_credit_card_not_registered(self):
        cc = CreditCardPayment("9999999999999999")
        self.assertFalse(cc.validate())


class TestPayPalPayment(unittest.TestCase):
    def test_valid_paypal_email(self):
        pp = PayPalPayment("juan.delacruz@example.com")
        self.assertTrue(pp.validate())

    def test_invalid_missing_at_symbol(self):
        pp = PayPalPayment("juandelacruzexample.com")
        self.assertFalse(pp.validate())

    def test_invalid_missing_dot_after_at(self):
        pp = PayPalPayment("juan.delacruz@examplecom")
        self.assertFalse(pp.validate())

    def test_not_registered_email(self):
        pp = PayPalPayment("someone@unknown.com")
        self.assertFalse(pp.validate())


class TestCryptoPayment(unittest.TestCase):
    def test_valid_crypto_id(self):
        cp = CryptoPayment("id_33333")
        self.assertTrue(cp.validate())

    def test_invalid_format(self):
        cp = CryptoPayment("xx_33333")
        self.assertFalse(cp.validate())

    def test_invalid_length(self):
        cp = CryptoPayment("id_123")
        self.assertFalse(cp.validate())

    def test_wallet_not_registered(self):
        cp = CryptoPayment("id_99999")
        self.assertFalse(cp.validate())


class TestCheckoutFunction(unittest.TestCase):
    def test_checkout_valid_credit(self):
        cc = CreditCardPayment("1111111111111111")
        captured_output = StringIO()
        sys.stdout = captured_output
        checkout(cc, 1000)
        sys.stdout = sys.__stdout__
        self.assertIn("Payment successful", captured_output.getvalue())

    def test_checkout_invalid_credit(self):
        cc = CreditCardPayment("9999")
        captured_output = StringIO()
        sys.stdout = captured_output
        checkout(cc, 1000)
        sys.stdout = sys.__stdout__
        self.assertNotIn("Payment successful", captured_output.getvalue())


if __name__ == "__main__":
    unittest.main()
