from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscribe, name='subscribe'),
    path('create_subscription/', views.create_customer_and_subscription,
         name='create_subscription'),
]
