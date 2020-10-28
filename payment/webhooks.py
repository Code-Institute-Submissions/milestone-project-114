from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from payment.webhook_handler import StripeSubscriptionWebhookHandler
import stripe


@require_POST
@csrf_exempt
def subscribe_webhook(request):
    """ Catch the stripe subscription webhooks """
    # Set up
    webhook_secret = settings.SUBSCRIBE_WEBHOOK_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Get the webhook data and verify it's signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload,
            sig_header,
            webhook_secret,
        )

    except ValueError as e:
        # Invalid payload
        return HttpResponse(content=e, status=400)

    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(content=e, status=400)

    except Exception as e:
        return HttpResponse(content=e, status=400)

    # Set up the webhook handler
    handler = StripeSubscriptionWebhookHandler(request)

    # Map the webhook events to the relevant handler functions in the handler
    event_map = {
        'invoice.paid': handler.handle_invoice_paid,
        'invoice.payment_failed': handler.handle_invoice_payment_failed,
        'customer.subscription.deleted': handler.handle_subscription_deleted,
    }

    # Get the webhook type
    event_type = event['type']

    # If handler exists, retrieve from the event map
    # Default set to generic handler
    event_handler = event_map.get(event_type, handler.handle_event)

    # Call the handler with the relevant event
    response = event_handler(event)
    return response























'''from profiles.models import UserProfile
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import stripe
from subscriptions.models import Pricing
from django.contrib import messages


@require_POST
@csrf_exempt
def subscribe_webhook(request):
    """ Catch the stripe subscription webhooks """
    webhook_secret = settings.SUBSCRIBE_WEBHOOK_SECRET
    payload = request.body
    signature = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload=payload,
            sig_header=signature,
            secret=webhook_secret
        )
        data = event['data']

    except Exception as e:
        return HttpResponse(content=e, status=400)

    # Get the type of webhook event sent -
    # used to check the status of PaymentIntents.
    event_type = event['type']

    if event_type == 'invoice.paid':
        # Used to provision services after the trial has ended.
        # The status of the invoice will show up
        # as paid. Store the status in your
        # database to reference when a user
        # accesses your service to avoid hitting rate
        # limits.
        webhook_object = data['object']
        stripe_customer_id = webhook_object['customer']
        userprofile = UserProfile.objects.get(stripe_customer_id=stripe_customer_id)
        userprofile.user.subscription.stripe_subscription_id = webhook_object['subscription']
        stripe_sub = stripe.Subscription.retrieve(webhook_object['subscription'])
        stripe_price_id = stripe_sub['plan']['id']
        pricing = Pricing.objects.get(stripe_price_id=stripe_price_id)
        userprofile.user.subscription.status = webhook_object['status']
        userprofile.user.subscription.pricing = pricing
        userprofile.user.subscription.save()
        messages.success(
            request,
            'Congratulations! Your paid subscription is now active.'
        )

    if event_type == 'invoice.payment_failed':
        # If the payment fails or the customer
        # does not have a valid payment method,
        # an invoice.payment_failed event is sent,
        # the subscription becomes past_due.
        # Use this webhook to notify your user that their payment has
        # failed and to retrieve new card details.
        messages.warning(
            request,
            'Payment for subscription failed. Please try again.'
        )

    if event_type == 'customer.subscription.deleted':
        webhook_object = data['object']
        stripe_customer_id = webhook_object['customer']
        stripe_sub = stripe.Subscription.retrieve(webhook_object['id'])
        userprofile = UserProfile.objects.get(stripe_customer_id=stripe_customer_id)
        userprofile.user.subscription.status = stripe_sub['status']
        userprofile.user.subscription.save()
        messages.success(
            request,
            'You have successfully cancelled your subscription.'
        )

    return HttpResponse()'''
