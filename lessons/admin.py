from django.contrib import admin
from .models import Artist, MasterclassOverview


class ArtistAdmin(admin.ModelAdmin):
    list_display = (
        'artist_friendly_name',
    )

    ordering = ('artist_friendly_name',)


admin.site.register(Artist, ArtistAdmin)
admin.site.register(MasterclassOverview)
