from django.contrib import admin
from .models import Merch


class MerchAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'price',
        'image',
    )

    ordering = ('id',)


admin.site.register(Merch, MerchAdmin)
