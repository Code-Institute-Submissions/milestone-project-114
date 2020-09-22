from django.shortcuts import render, get_object_or_404
from .models import Artist, MasterclassOverview, Masterclass


def masterclasses(request):
    """ View to render the masterclasses page """

    artists = Artist.objects.all()
    overviews = MasterclassOverview.objects.all()

    context = {
        'artists': artists,
        'overviews': overviews,
    }

    return render(request, 'lessons/masterclasses.html', context)


def masterclass(request, masterclass_title):
    """ View to render the masterclass lessons page """

    masterclass = get_object_or_404(MasterclassOverview, masterclass_title=masterclass_title)
    artist = get_object_or_404(Artist)

    overviews = MasterclassOverview.objects.all()
    lessons = Masterclass.objects.all()

    context = {
        'masterclass': masterclass,
        'artist': artist,
        'overviews': overviews,
        'lessons': lessons,
    }

    return render(request, 'lessons/masterclass.html', context)
