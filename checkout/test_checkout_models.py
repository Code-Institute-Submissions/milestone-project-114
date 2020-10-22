from django.test import TestCase
from .models import Order


class TestCheckoutModels(TestCase):

    def test_order_id_defaults_to_true(self):
        order = Order.objects.create(order_number='1234')
        self.assertTrue(order.id)

    def test_order_string_method_returns_order_number(self):
        order = Order.objects.create(order_number='1234')
        self.assertEqual(str(order), '1234')
