from django import template


register = template.Library()


@register.filter(name='calculate_subtotal')
def calculate_subtotal(price, quantity):
    """ Calculate the subtotal of quantity of items """
    return price * quantity
