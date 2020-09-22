from django.shortcuts import render


def view_cart(request):
    """ View to render the subscription/merch cart """
    return render(request, 'cart/cart.html')
