from django.test import TestCase
from djkatta.accounts.utils import generate_random_string


class AccountsTests(TestCase):

    def test_landing_page(self):
        response = self.client.get('/')
        self.assertEqual(200, response.status_code)
