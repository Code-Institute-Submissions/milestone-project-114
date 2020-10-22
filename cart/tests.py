from django.test import TestCase


class TestCartContexts(TestCase):

    def test_user_subscription_status(self):
        status = 'paid'

        if status == 'paid':
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
