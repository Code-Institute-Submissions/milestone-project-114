from django.shortcuts import render
import stripe
import json
import djstripe
from django.http.response import JsonResponse, HttpResponse
from djstripe.models import Product
from django.contrib.auth.decorators import login_required
from .models import Subscription
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


@login_required
def subscribe(request):
    """ View to render the subscription page """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

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
        'stripe_public_key': stripe_public_key,
    }

    return render(request, 'subscribe/subscribe.html', context)
