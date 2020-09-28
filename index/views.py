from django.shortcuts import render
from .models import Features


def index(request):
    """ View to render the home page """

    features = Features.objects.all().order_by('id').reverse()

    context = {
        'features': features,
    }

    return render(request, 'index/index.html', context)
