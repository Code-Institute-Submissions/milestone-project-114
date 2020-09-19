from django.shortcuts import render


def index(request):
    """ View to render the home page """
    return render(request, 'index/index.html')
