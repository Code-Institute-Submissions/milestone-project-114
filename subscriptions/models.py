from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from allauth.account.signals import email_confirmed
from django.contrib.auth.signals import user_logged_in
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


class Pricing(models.Model):

    class Meta:
        verbose_name_plural = 'Pricing'

    name = models.CharField(max_length=50)
    stripe_price_id = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pricing = models.ForeignKey(
        Pricing,
        on_delete=models.CASCADE,
        related_name='subscriptions'
    )
    created = models.DateTimeField(auto_now_add=True)
    stripe_subscription_id = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.user.email


def post_email_confirmed(request, email_address, *args, **kwargs):
    user = User.objects.get(email=email_address.email)
    signup_free = Pricing.objects.get(name='Signup Free')
    subscription = Subscription.objects.create(
        user=user,
        pricing=signup_free,
    )
    stripe_customer = stripe.Customer.create(
        email=user.email
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
    user.userprofile.save()


def user_logged_in_receiver(sender, user, **kwargs):
    subscription = user.subscription
    sub = stripe.Subscription.retrieve(
        subscription.stripe_subscription_id
    )

    subscription.status = sub['status']
    subscription.save()


user_logged_in.connect(user_logged_in_receiver)
email_confirmed.connect(post_email_confirmed)
