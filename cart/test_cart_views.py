from django.test import TestCase
from merch.models import Merch


class TestCartViews(TestCase):

    def test_get_cart(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')