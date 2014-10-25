from django.test import TestCase
from random import randrange


def generate_random_string(chars=6):
    """Returns a random string of length `chars`"""
    return '%x'%randrange(16**chars)


class AccountsTests(TestCase):

    def test_landing_page(self):
        response = self.client.get('/')
        self.assertEqual(200, response.status_code)
