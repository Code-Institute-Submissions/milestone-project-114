from django.shortcuts import render
import stripe
import json
import djstripe
from django.http import JsonResponse, HttpResponse
from djstripe.models import Product
from django.contrib.auth.decorators import login_required
from .models import Subscription


@login_required
def subscribe(request):
    """ View to render the subscription page """

    subscriptions = Subscription.objects.all()
    monthly_prices = []

    if subscriptions:
        for price in subscriptions:
            monthly_prices.append(int(price.monthly_price))

        price1 = monthly_prices[0]
        price2 = monthly_prices[1]

        percentage_saved = ((price1 - price2)/((price1 + price2) / 2) * 100)
    else:
        return render(request, 'index/index.html')

    products = Product.objects.all()

    context = {
        'subscriptions': subscriptions,
        'percentage_saved': percentage_saved,
        'products': products,
    }

    return render(request, 'subscribe/subscribe.html', context)


@login_required
def create_sub(request):
    if request.method == 'POST':
        # Reads application/json and returns a response
        data = json.loads(request.body)
        payment_method = data['payment_method']
        stripe.api_key = settings.STRIPE_SECRET_KEY

        payment_method_obj = stripe.PaymentMethod.retrieve(payment_method)
        djstripe.models.PaymentMethod.sync_from_stripe_data(payment_method_obj)


        try:
            # This creates a new Customer and attaches the PaymentMethod in one API call.
            customer = stripe.Customer.create(
                payment_method=payment_method,
                email=request.User.email,
                invoice_settings={
                    'default_payment_method': payment_method
                }
            )

            djstripe_customer = djstripe.models.Customer.sync_from_stripe_data(customer)
            request.user.customer = djstripe_customer

            # At this point, associate the ID of the Customer object with your
            # own internal representation of a customer, if you have one.
            print(customer)
            # Subscribe the user to the subscription created
            subscription = stripe.Subscription.create(
                customer=customer.id,
                items=[
                    {
                        "price": data["price_id"],
                    },
                ],
                expand=["latest_invoice.payment_intent"]
            )
            djstripe_subscription = djstripe.models.Subscription.sync_from_stripe_data(subscription)

            request.user.subscription = djstripe_subscription
            request.user.save()

            return JsonResponse(subscription)
        except Exception as e:
            return JsonResponse({'error': (e.args[0])}, status=403)
    else:
        return HttpResponse('request method not allowed')


def complete(request):
    return render(request, "complete.html")
