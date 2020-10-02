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
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified item to the shopping bag """

    item = get_object_or_404(Merch, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'item_size' in request.POST:
        size = request.POST['item_size']
    cart = request.session.get('cart', {})

    if size:
        if item_id in list(cart.keys()):
            if size in cart[item_id]['items_by_size'].keys():
                cart[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Updated size {size.upper()} {item.name} quantity to {cart[item_id]["items_by_size"][size]}')
            else:
                cart[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} {item.name} to your cart')
        else:
            cart[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size {size.upper()} {item.name} to your cart')
    else:
        if item_id in list(cart.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {item.name} quantity to {cart[item_id]}')
        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {item.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):

    item = get_object_or_404(Merch, pk=item_id)

    quantity = int(request.POST.get('quantity'))
    size = None
    if 'item_size' in request.POST:
        size = request.POST['item_size']
    cart = request.session.get('cart', {})

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

    try:
        item = get_object_or_404(Merch, pk=item_id)
        size = None
        if 'item_size' in request.POST:
            size = request.POST['item_size']
        cart = request.session.get('cart', {})

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
