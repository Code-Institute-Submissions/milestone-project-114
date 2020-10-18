from django.urls import path
from . import views

app_name = 'payment'


urlpatterns = [
    path('subscribe/', views.subscribe, name='subscribe'),
    path(
        'create-subscription/',
        views.createSubscription,
        name='create-subscription'
    ),
    path('retry-invoice/', views.retrySubscription, name='retry-invoice'),
]
