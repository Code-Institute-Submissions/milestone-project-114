from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
    HttpResponse
)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from merch.models import Merch
from .models import Order, OrderLineItem
from cart.contexts import cart_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        payment_id = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(
            payment_id,
            metadata={
                'cart': json.dumps(request.session.get('cart', {})),
                'save_info': request.POST.get('save_info'),
                'username': request.user,
            }
        )
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(
            request,
            'Sorry, your payment cannot be\
            processed at this time. Please try again later.'
        )
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            payment_id = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_payment_id = payment_id
            order.original_cart = json.dumps(cart)
            order.save()
            for item_id, item_data in cart.items():
                try:
                    item = Merch.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            item=item,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                item=item,
                                quantity=quantity,
                                item_size=size
                            )
                            order_line_item.save()
                except Merch.DoesNotExist:
                    messages.error(
                        request,
                        (
                            "One of the merch items in your shopping\
                                 cart wasn't found in out database."
                        )
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(
                reverse(
                    'checkout_suceess',
                    args=[order.order_number]
                )
            )
        else:
            messages.error(
                request,
                "There was an error wwith your form submission"
            )
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(
                request,
                "Looks like there's nothing in your cart right now!"
            )
            return redirect(reverse('merch'))

        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing.')

    template = 'checkout/checkout.html'

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(
        request,
        f'Order processed successfully! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}'
    )

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'

    context = {
        'order': order,
    }

    return render(request, template, context)
