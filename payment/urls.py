from django.urls import path
from . import views
from .webhooks import subscribe_webhook

app_name = 'payment'


urlpatterns = [
    path('subscribe/', views.subscribe, name='subscribe'),
    path('create-subscription/', views.createSubscription, name='create-subscription'),
    path('retry-invoice/', views.retrySubscription, name='retry-invoice'),
    path('webhook/', subscribe_webhook, name='webhook'),
]
