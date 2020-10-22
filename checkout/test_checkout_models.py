from django.test import TestCase
from .models import Order, OrderLineItem


class TestCheckoutModels(TestCase):

    def test_order_id_defaults_to_true(self):
        order = Order.objects.create(order_number=1234)
        self.assertTrue(order.id)
