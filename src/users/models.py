from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    ROLE_CHOICES = [
        ("S", "Super User"),
        ("U", "User"),
        ("A", "Admin")
    ]

    balance = models.FloatField()
    fastbuy_code = models.CharField(max_length=6)
    role = models.CharField(max_length=1, choices=ROLE_CHOICES)

    def __str__(self):
        return str(self.username)

    @property
    def user_balance(self):
        "Returns the user balance"
        balance = format(self.balance, '-.2f').replace(".", ",")
        return balance

    @user_balance.setter
    def user_balance(self, value):
        self._user_balance = value
