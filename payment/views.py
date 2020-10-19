from django.shortcuts import render
from profiles.models import UserProfile
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import stripe
import json
from djstripe.models import Product
from django.contrib.auth.decorators import login_required
from subscriptions.models import Pricing

stripe.api_key = settings.STRIPE_SECRET_KEY


@csrf_exempt
def webhook(request):
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
        return e
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
        userprofile.user.subscription.status = webhook_object['status']
        stripe_price_id = stripe_sub['plan']['id']

        pricing = Pricing.objects.get(stripe_price_id=stripe_price_id)
        userprofile.user.subscription.pricing = pricing

        userprofile.user.subscription.save()

    if event_type == 'invoice.payment_failed':
        # If the payment fails or the customer
        # does not have a valid payment method,
        # an invoice.payment_failed event is sent,
        # the subscription becomes past_due.
        # Use this webhook to notify your user that their payment has
        # failed and to retrieve new card details.
        print(data)

    if event_type == 'customer.subscription.deleted':

        webhook_object = data['object']
        stripe_customer_id = webhook_object['customer']
        stripe_sub = stripe.Subscription.retrieve(webhook_object['id'])
        userprofile = UserProfile.objects.get(stripe_customer_id=stripe_customer_id)
        userprofile.user.subscription.status = stripe_sub['status']
        userprofile.user.subscription.save()

    return HttpResponse()


@login_required
def subscribe(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    client_secret = settings.STRIPE_SECRET_KEY
    customer_id = request.user.userprofile.stripe_customer_id

    products = Product.objects.all()

    context = {
        'stripe_public_key': stripe_public_key,
        'stripe_secret_key': client_secret,
        'products': products,
        'customer_id': customer_id,
    }

    return render(request, 'payment/subscribe.html', context)


def createSubscription(request, *args, **kwargs):
    data = json.loads(request.body)
    customer_id = request.user.userprofile.stripe_customer_id

    try:
        # Attach the payment method to the customer
        stripe.PaymentMethod.attach(
            data['paymentMethodId'],
            customer=customer_id,
        )
        # Set the default payment method on the customer
        stripe.Customer.modify(
            customer_id,
            invoice_settings={
                'default_payment_method': data['paymentMethodId'],
            },
        )

        # Create the subscription
        subscription = stripe.Subscription.create(
            customer=customer_id,
            items=[
                {
                    'price': data['priceId'],
                }
            ],
            expand=['latest_invoice.payment_intent'],
        )

        data = {}
        data.update(subscription)

        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({
            'error': {'message': str(e)}
        })


def retrySubscription(request, *args, **kwargs):
    data = json.loads(request.body)
    customer_id = request.user.userprofile.stripe_customer_id
    try:

        stripe.PaymentMethod.attach(
            data['paymentMethodId'],
            customer=customer_id,
        )
        # Set the default payment method on the customer
        stripe.Customer.modify(
            customer_id,
            invoice_settings={
                'default_payment_method': data['paymentMethodId'],
            },
        )

        invoice = stripe.Invoice.retrieve(
            data['invoiceId'],
            expand=['payment_intent'],
        )
        data = {}
        data.update(invoice)

        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({
            'error': {'message': str(e)}
        })
