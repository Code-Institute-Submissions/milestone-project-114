from django.shortcuts import render
from .models import Subscription


def subscribe(request):
    """ View to render the subscription page """

    subscriptions = Subscription.objects.all()

    context = {
        'subscriptions': subscriptions,
    }

    return render(request, 'subscribe/subscribe.html', context)
