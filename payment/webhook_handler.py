from django.http import HttpResponse
from profiles.models import UserProfile
from subscriptions.models import Pricing
from django.contrib import messages
import stripe
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail


class StripeSubscriptionWebhookHandler:
    """ Handle subscription webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handle generic events """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200,
        )

    def _send_confirmation_email(self, subscription):
        """ Send a confirmation email to customer on success of payment """
        customer_email = UserProfile.email
        subject = render_to_string(
            'payment/emails/email_subject.txt',
            {
                'subscription': subscription,
            },
        )
        body = render_to_string(
            'payment/emails/email_body.txt',
            {
                'subscription': subscription,
                'contact_email': settings.DEFAULT_EMAIL,
            },
        )
        send_mail(
            subject,
            body,
            settings.DEFAULT_EMAIL,
            [customer_email],
        )

    def handle_invoice_paid(self, request, event):
        """ Handle the invoice.paid stripe webhook """

        # Used to provision services after the trial has ended.
        # The status of the invoice will show up
        # as paid.
        webhook_object = event.data.object
        stripe_customer_id = webhook_object['customer']
        userprofile = UserProfile.objects.get(stripe_customer_id=stripe_customer_id)
        userprofile.user.subscription.stripe_subscription_id = webhook_object['subscription']
        stripe_sub = stripe.Subscription.retrieve(webhook_object['subscription'])
        stripe_price_id = stripe_sub['plan']['id']
        pricing = Pricing.objects.get(stripe_price_id=stripe_price_id)
        userprofile.user.subscription.status = webhook_object['status']
        userprofile.user.subscription.pricing = pricing
        userprofile.user.subscription.save()
        subscription = userprofile.user.subscription
        messages.success(
            request,
            'Congratulations! Your paid subscription is now active.'
        )

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200,
        )

        self._send_confirmation_email(subscription)
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200,
        )

    def handle_invoice_payment_failed(self, request, event):
        """ Handle the invoice.payment_failed stripe webhook """

        # If the payment fails or the customer
        # does not have a valid payment method,
        # an invoice.payment_failed event is sent,
        # the subscription becomes past_due.
        messages.warning(
            request,
            'Payment for subscription failed. Please try again.'
        )

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200,
        )

    def handle_subscription_deleted(self, request, event):
        """ Handle the customer.subscription.deleted stripe webhook """

        webhook_object = event.data.object
        stripe_customer_id = webhook_object['customer']
        stripe_sub = stripe.Subscription.retrieve(webhook_object['id'])
        userprofile = UserProfile.objects.get(stripe_customer_id=stripe_customer_id)
        userprofile.user.subscription.status = stripe_sub['status']
        userprofile.user.subscription.save()
        messages.success(
            request,
            'You have successfully cancelled your subscription.'
        )

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200,
        )
