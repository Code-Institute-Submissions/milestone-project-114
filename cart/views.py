from django.shortcuts import (
    render,
    redirect,
    reverse,
    HttpResponse,
    get_object_or_404
)
from django.contrib import messages
from merch.models import Merch


def view_cart(request):
    """ View to display the cart template """
    template = 'cart/cart.html'
    return render(request, template)


def add_to_cart(request, item_id):
    """ Add a quantity of the specified item to the shopping cart """
    item = get_object_or_404(Merch, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None

    """ If the item has a size, define the size
        variable to be used """
    if 'item_size' in request.POST:
        size = request.POST['item_size']

    cart = request.session.get('cart', {})

    """ If any items with a size exists,
        add the item to the cart, otherwise
        add an item without a size to the cart """
    if size:
        if item_id in list(cart.keys()):
            if size in cart[item_id]['items_by_size'].keys():
                cart[item_id]['items_by_size'][size] += quantity
                messages.success(
                    request,
                    f'Updated size {size.upper()} {item.name} quantity\
                         to {cart[item_id]["items_by_size"][size]}'
                )
            else:
                cart[item_id]['items_by_size'][size] = quantity
                messages.success(
                    request,
                    f'Added size {size.upper()} {item.name} to your cart'
                )
        else:
            cart[item_id] = {'items_by_size': {size: quantity}}
            messages.success(
                request,
                f'Added size {size.upper()} {item.name} to your cart'
            )
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(
                request,
                f'Updated {item.name} quantity to {cart[item_id]}'
            )
        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {item.name} to your cart')

    request.session['cart'] = cart

    return redirect(redirect_url)


def update_cart(request, item_id):
    """ Update the cart by the specified quantity of a specific product """
    item = get_object_or_404(Merch, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None

    """ If the item has a size, define the size
        variable to be used """
    if 'item_size' in request.POST:
        size = request.POST['item_size']

    cart = request.session.get('cart', {})

    """ If any items with a size exists,
        update the item in the cart, otherwise
        update the item without a size in the cart """
    if size:
        if quantity > 0:
            cart[item_id]['items_by_size'][size] = quantity
            messages.success(
                request,
                f'Updated size {size.upper()} {item.name}\
                quantity of {cart[item_id]["items_by_size"][size]}!'
            )
        else:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
            messages.success(
                request,
                f'Removed size {size.upper()} {item.name} from the cart!'
            )
    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(
                request, f'Updated {item.name} quantity of {cart[item_id]}'
            )
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {item.name} from the cart!')

    request.session['cart'] = cart

    return redirect(reverse('view_cart'))


def delete_from_cart(request, item_id):
    """ Delete a specified item from the cart """
    try:
        item = get_object_or_404(Merch, pk=item_id)
        size = None

        """ If the item has a size, define the size
        variable to be used """
        if 'item_size' in request.POST:
            size = request.POST['item_size']

        cart = request.session.get('cart', {})

        """ If any items with a size exists,
        delete the item from the cart, otherwise
        delete the item without a size from the cart """
        if size:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
            messages.success(
                request,
                f'Removed size {size.upper()} {item.name} from the cart!'
            )
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {item.name} from the cart!')

        request.session['cart'] = cart

        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')

        return HttpResponse(status=500)
