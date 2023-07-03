from django.test import TestCase
from ..models import User


class UserTestCase(TestCase):
    def test_balance_is_formmated_pos(self):
        user = User(balance=15)
        self.assertEqual(user.user_balance, '15,00')

    def test_balance_is_formmated_neg(self):
        user = User(balance=-1234)
        self.assertEqual(user.user_balance, '-1234,00')
