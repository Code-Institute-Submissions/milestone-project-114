from django.test import TestCase
from .models import Pricing, Subscription
from django.contrib.auth.models import User


class TestSubscriptionshModels(TestCase):

    def test_pricing_id_defaults_to_true(self):
        pricing_tier = Pricing.objects.create(name='Test Pricing')
        self.assertTrue(pricing_tier.id)

    def test_subscription_id_defaults_to_true(self):
        pricing = Pricing.objects.create(name='Test Pricing')
        pricing = Pricing.objects.get(name='Test Pricing')

        user = User.objects.create(email='Test Email')
        user = User.objects.get(email='Test Email')

        subscription = Subscription.objects.create(
            pricing=pricing,
            user=user
            )
        self.assertTrue(subscription.id)
