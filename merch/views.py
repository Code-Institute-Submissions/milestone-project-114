from django.shortcuts import render, get_object_or_404
from .models import Merch


def all_merch(request):
    """ View to render all of the merch """

    merch = Merch.objects.all()

    context = {
        'merch': merch,
    }

    return render(request, 'merch/store.html', context)


def item_detail(request, item_id):
    """ View to render the merch item details """

    item = get_object_or_404(Merch, pk=item_id)

    context = {
        'item': item,
    }

    return render(request, 'merch/item_detail.html', context)
