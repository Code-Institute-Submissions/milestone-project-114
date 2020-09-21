from django.shortcuts import render
from .models import Merch


def all_merch(request):
    """ View to render all of the merch """

    merch = Merch.objects.all()

    context = {
        'merch': merch,
    }

    return render(request, 'merch/store.html', context)
