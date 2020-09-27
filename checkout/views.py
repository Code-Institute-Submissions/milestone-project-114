from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(
            request,
            "Looks like there's nothing in your cart right now!"
        )
        return redirect(reverse('merch'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'

    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HQ8d2EjKkX6AQGJ2OLLgzYbVf1rdvwRXRSM587Tm1CbjtEzOK8txcELxpQZ247RqTSArIgrST7KhDwcSPanA5Rw00kTCvgs02',
        'client_secret': 'secret',
    }

    return render(request, template, context)
