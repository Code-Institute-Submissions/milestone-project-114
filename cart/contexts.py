from django.shortcuts import get_object_or_404
from decimal import Decimal
from django.conf import settings
from merch.models import Merch


def cart_contents(request):

    cart_items = []
    total = 0
    item_count = 0
    delivery = total * Decimal(settings.DELIVERY_PERCENTAGE)
    grand_total = total + delivery
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        item = get_object_or_404(Merch, pk=item_id)
        total += quantity * item.price
        item_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'item': item,
        })

    context = {
        'cart_items': cart_items,
        'total': total,
        'item_count': item_count,
        'delivery': delivery,
        'grand_total': grand_total
    }

    return context
