from django.urls import path
from . import views

app_name = 'subscribe'

urlpatterns = [
    path('', views.subscriptions, name='subscriptions'),
    path('create_subscription/', views.create_customer_and_subscription,
         name='create_subscription'),
]
