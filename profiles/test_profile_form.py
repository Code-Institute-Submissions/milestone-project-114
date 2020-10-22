from django.test import TestCase
from .forms import UserProfileForm


class TestProfileForm(TestCase):

    def test_excluded_fields(self):
        profile_form = UserProfileForm()
        self.assertEqual(
            profile_form.Meta.exclude, ('user', 'stripe_customer_id',)
        )
