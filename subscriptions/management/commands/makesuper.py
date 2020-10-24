import stripe
import random
import string
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from subscriptions.models import Pricing, Subscription

User = get_user_model()
stripe.api_key = settings.STRIPE_SECRET_KEY


def randomString(stringLength=20):
    password_characters = string.ascii_letters + string.digits + string.punctuation

    return ''.join(
        random.choice(password_characters) for i in range(stringLength))


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if not User.objects.filter(username="admin").exists():
            if settings.DEBUG:
                password = 'admin'
            else:
                password = randomString()
            user = User.objects.create_superuser(
                'admin', 'admin@admin.com', password
            )

            free_trial_pricing = Pricing.objects.get(name='Signup Free')
            subscription = Subscription.objects.create(
                user=user,
                pricing=free_trial_pricing,
            )

            stripe_customer = stripe.Customer.create(
                email=user.email,
            )

            stripe_subscription = stripe.Subscription.create(
                customer=stripe_customer['id'],
                items=[
                    {
                        'price': 'price_1HcZWtEjKkX6AQGJldgbPRLj'
                    }
                ],
            )

            subscription.status = stripe_subscription['status']
            subscription.stripe_subscription_id = stripe_subscription['id']
            subscription.save()
            user.userprofile.stripe_customer_id = stripe_customer['id']
            user.userporfile.save()
