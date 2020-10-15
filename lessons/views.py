from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Artist, MasterclassOverview
from django.contrib.auth.decorators import login_required


def masterclasses(request):
    """ View to render the masterclasses page """

    artists = Artist.objects.all()
    overviews = MasterclassOverview.objects.all()

    # Search set to none so page is able to load without search
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

    context = {
        'artists': artists,
        'overviews': overviews,
        'search_query': search,
    }

    return render(request, 'lessons/masterclasses.html', context)


@login_required
def masterclass(self, request, masterclass_title):
    """ View to render the masterclass lessons page """

    masterclass = get_object_or_404(
        MasterclassOverview,
        masterclass_title=masterclass_title
    )

    overviews = MasterclassOverview.objects.all()

    context = {
        'masterclass': masterclass,
        'overviews': overviews,
    }

    return render(request, 'lessons/masterclass.html', context)
