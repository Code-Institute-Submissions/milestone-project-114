from django.contrib import admin
from .models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'monthly_price',
        'yearly_price',
        'frequency',
        'paid',
    )


admin.site.register(Subscription, SubscriptionAdmin)
