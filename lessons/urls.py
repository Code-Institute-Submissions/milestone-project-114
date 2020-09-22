from django.urls import path
from . import views

urlpatterns = [
    path('', views.masterclasses, name='masterclasses'),
    path('<masterclass_title>', views.masterclass, name='masterclass'),
]
