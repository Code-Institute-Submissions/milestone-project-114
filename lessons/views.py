from django.shortcuts import render, get_object_or_404
"""
from django.shortcuts import redirect, reverse
from django.contrib import messages
from django.db.models import Q
"""
from .models import Artist, MasterclassOverview


def masterclasses(request):
    """ View to render the masterclasses page """
    template = 'lessons/masterclasses.html'
    artists = Artist.objects.all()
    overviews = MasterclassOverview.objects.all()

    """
        Search result function made redundant as
        not necessary for the scope of the project
    """
    """
    search = None

    if request.GET:
        if 'search' in request.GET:
            search = request.GET['search']
            if not search:
                messages.error(
                    request,
                    "You didn't enter any search criteria."
                )
                messages.error(
                    request,
                    "You didn't enter any search criteria!"
                )
                return redirect(reverse('masterclasses'))

            searches = Q(
                name__icontains=search) | Q(description__icontains=search)
            overviews = overviews.filter(searches)
    """

    context = {
        'artists': artists,
        'overviews': overviews,
    }

    return render(request, template, context)


def masterclass(request, masterclass_title):
    """ View to render the masterclass lessons page """
    template = 'lessons/masterclass.html'
    masterclass = get_object_or_404(
        MasterclassOverview,
        masterclass_title=masterclass_title
    )
    overviews = MasterclassOverview.objects.all()
    context = {
        'masterclass': masterclass,
        'overviews': overviews,
    }

    return render(request, template, context)
