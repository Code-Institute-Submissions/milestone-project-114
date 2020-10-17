from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def subscribe(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    client_secret = settings.STRIPE_SECRET_KEY

    context = {
        'stripe_public_key': stripe_public_key,
        'stripe_secret_key': client_secret,
    }

    return render(request, 'payment/subscribe.html', context)


def createSubscription(self, request, *args, **kwargs):
    data = request.POST
    customer_id = request.user.stripe_customer_id

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


def retrySubscription(self, request, *args, **kwargs):
    data = request.POST
    customer_id = request.user.stripe_customer_id
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
