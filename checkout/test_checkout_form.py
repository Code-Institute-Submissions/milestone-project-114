from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):

    def test_full_name_is_required(self):
        order_form = OrderForm({'full_name': ''})
        self.assertFalse(order_form.is_valid())
        self.assertIn('full_name', order_form.errors.keys())
        self.assertEqual(
            order_form.errors['full_name'][0],
            'This field is required.'
        )

    def test_email_is_not_required(self):
        order_form = OrderForm({'email': ''})
        self.assertTrue(order_form.is_valid)

    def test_phone_number_is_required(self):
        order_form = OrderForm({'phone_number': ''})
        self.assertFalse(order_form.is_valid())
        self.assertIn('phone_number', order_form.errors.keys())
        self.assertEqual(
            order_form.errors['phone_number'][0],
            'This field is required.'
        )

    def test_street_address_1_is_required(self):
        order_form = OrderForm({'street_address1': ''})
        self.assertFalse(order_form.is_valid())
        self.assertIn('street_address1', order_form.errors.keys())
        self.assertEqual(
            order_form.errors['street_address1'][0],
            'This field is required.'
        )

    def test_street_address_2_is_not_required(self):
        order_form = OrderForm({'street_address2': ''})
        self.assertTrue(order_form.is_valid)

    def test_town_or_city_is_required(self):
        order_form = OrderForm({'town_or_city': ''})
        self.assertFalse(order_form.is_valid())
        self.assertIn('town_or_city', order_form.errors.keys())
        self.assertEqual(
            order_form.errors['town_or_city'][0],
            'This field is required.'
        )

    def test_postcode_is_not_required(self):
        order_form = OrderForm({'postcode': ''})
        self.assertTrue(order_form.is_valid)

    def test_country_is_required(self):
        order_form = OrderForm({'country': ''})
        self.assertFalse(order_form.is_valid())
        self.assertIn('country', order_form.errors.keys())
        self.assertEqual(
            order_form.errors['country'][0],
            'This field is required.'
        )

    def test_county_is_not_required(self):
        order_form = OrderForm({'county': ''})
        self.assertTrue(order_form.is_valid)

    def test_fields_in_meta(self):
        order_form = OrderForm()
        self.assertEqual(
            order_form.Meta.fields, (
                'full_name',
                'email',
                'phone_number',
                'street_address1',
                'street_address2',
                'town_or_city',
                'postcode',
                'country',
                'county',
            )
        )
