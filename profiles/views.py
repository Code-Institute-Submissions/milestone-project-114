from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.conf import settings
from checkout.models import Order
from django.http import JsonResponse
from django.contrib.auth.models import User
from subscriptions.models import Pricing, Subscription
from .models import UserProfile
from .forms import UserProfileForm
import stripe
import json

stripe.api_key = settings.STRIPE_SECRET_KEY


def profile(request):
    """ View to render the profile page """
    template = 'profiles/profile.html'
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    context = {
        'profile': profile,
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)


def order_history(request, order_number):
    """ Display the user's order history in the profile view """
    template = 'checkout/checkout_success.html'
    order = get_object_or_404(Order, order_number=order_number)
    messages.info(
        request,
        f'This is a previous order confirmation for order {order_number}.'
    )
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


def cancelSubscription(request, *args, **kwargs):
    """ Cancel the user's subscription on the backend """
    data = json.loads(request.body)

    try:
        """ Cancel the subscription by deleting it """
        deletedSubscription = stripe.Subscription.delete(
            data['subscriptionId']
        )
        messages.success(
            request,
            "You have successfully cancelled your subscription."
        )

        return JsonResponse(deletedSubscription)

    except Exception as e:
        return JsonResponse(error=str(e)), 403

    return redirect(reverse('profile'))
