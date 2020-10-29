from django.test import TestCase


class TestContexts(TestCase):

    def test_user_subscription_status(self):
        test_status = 'paid'

        if test_status == 'paid':
            total = 10
            delivery = total * (10 / 100)
            discount = total * (10 / 100)
            grand_total = delivery + total - discount
            self.assertEqual(grand_total, 10)
        else:
            total = 10
            delivery = total * (10 / 100)
            grand_total = delivery + total
            self.assertEqual(grand_total, 11)


class TestCartTools(TestCase):

    def test_cart_tools(self):
        price = 5
        quantity = 3
        subtotal = price * quantity
        self.assertEqual(subtotal, 15)
