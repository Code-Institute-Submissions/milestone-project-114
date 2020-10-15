from django.contrib import admin
from .models import Pricing, Subscription


class PricingAdmin(admin.ModelAdmin):
    verbose_name = (
        'Pricing'
    )


admin.site.register(Pricing, PricingAdmin)
admin.site.register(Subscription)
