from decimal import Decimal
from django.conf import settings


def cart_contents(request):

    cart_items = []
    total = 0
    item_count = 0
    delivery = total * Decimal(settings.DELIVERY_PERCENTAGE)
    grand_total = total + delivery

    context = {
        'cart_items': cart_items,
        'total': total,
        'item_count': item_count,
        'delivery': delivery,
        'grand_total': grand_total
    }

    return context
