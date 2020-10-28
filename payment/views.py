from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
import stripe
import json
from djstripe.models import Product
from django.contrib.auth.decorators import login_required

stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def subscribe(request):
    """ View to render the subscribe page """
    template = 'payment/subscribe.html'
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

    return render(request, template, context)


def createSubscription(request, *args, **kwargs):
    """ Create the subscription on the backend """
    data = json.loads(request.body)
    customer_id = request.user.userprofile.stripe_customer_id

    try:
        """ Attach the payment method to the customer """
        stripe.PaymentMethod.attach(
            data['paymentMethodId'],
            customer=customer_id,
        )
        """ Set the default payment method on the customer """
        stripe.Customer.modify(
            customer_id,
            invoice_settings={
                'default_payment_method': data['paymentMethodId'],
            },
        )

        """ Create the subscription """
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
    """ Retry the subscription if invoice fails """
    data = json.loads(request.body)
    customer_id = request.user.userprofile.stripe_customer_id

    try:
        stripe.PaymentMethod.attach(
            data['paymentMethodId'],
            customer=customer_id,
        )

        """ Set the default payment method on the customer """
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
