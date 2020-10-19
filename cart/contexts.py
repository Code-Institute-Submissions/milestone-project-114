from django.shortcuts import get_object_or_404
from decimal import Decimal
from django.conf import settings
from merch.models import Merch


def cart_contents(request):

    cart_items = []
    total = 0
    item_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            item = get_object_or_404(Merch, pk=item_id)
            total += item_data * item.price
            item_count += item_data
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'item': item,
            })
        else:
            item = get_object_or_404(Merch, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * item.price
                item_count += quantity
                cart_items.append({
                    'item_id': item_id,
                    'quantity': item_data,
                    'item': item,
                    'size': size,
                })

    delivery = total * Decimal(settings.DELIVERY_PERCENTAGE / 100)

    if request.user.is_authenticated:
        discount = total * Decimal(settings.MEMBER_DISCOUNT / 100)

        grand_total = delivery + total - discount

        context = {
            'cart_items': cart_items,
            'total': total,
            'item_count': item_count,
            'delivery': delivery,
            'discount': discount,
            'grand_total': grand_total,
        }
    else:
        grand_total = delivery + total

        context = {
            'cart_items': cart_items,
            'total': total,
            'item_count': item_count,
            'delivery': delivery,
            'grand_total': grand_total,
        }

    return context
