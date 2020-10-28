from profiles.models import UserProfile
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

    return HttpResponse()
