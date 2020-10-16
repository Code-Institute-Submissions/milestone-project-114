from django.shortcuts import render
from django.conf import settings
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


def post(self, request, *args, **kwargs):
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
            data['customerId'],
            invoice_settings={
                'default_payment_method': data['paymentMethodId'],
            },
        )

        # Create the subscription
        subscription = stripe.Subscription.create(
            customer=data['customerId'],
            items=[
                {
                    'price': 'price_HGd7M3DV3IMXkC'
                }
            ],
            expand=['latest_invoice.payment_intent'],
        )
        return jsonify(subscription)
    except Exception as e:
        return jsonify(error={'message': str(e)}), 200

