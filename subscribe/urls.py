from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscribe, name='subscribe'),
    path('create-sub', views.create_sub, name='create_sub'),
    path('complete', views.complete, name='complete'),
]
