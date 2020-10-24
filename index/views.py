from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Features


def index(request):
    """ View to render the home page """
    """ Features redundant """
    template = 'index/index.html'
    features = Features.objects.all().order_by('id').reverse()
    context = {
        'features': features,
    }

    return render(request, template, context)


def features(request):
    """ View to render the features page (view now redundant) """
    template = 'index/features.html'
    features = Features.objects.all().order_by('id').reverse()
    paginator = Paginator(features, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'features': features,
        'page_obj': page_obj
    }

    return render(request, template, context)
