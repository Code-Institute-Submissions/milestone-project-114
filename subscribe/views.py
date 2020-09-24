from django.shortcuts import render
from .models import Subscription


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

    context = {
        'subscriptions': subscriptions,
        'percentage_saved': percentage_saved
    }

    return render(request, 'subscribe/subscribe.html', context)
