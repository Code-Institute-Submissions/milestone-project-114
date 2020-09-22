from django.contrib import admin
from .models import Artist, MasterclassOverview, Masterclass

class ArtistAdmin(admin.ModelAdmin):
    list_display = (
        'artist_friendly_name',
    )

    ordering = ('artist_friendly_name',)

class LessonAdmin(admin.ModelAdmin):
    list_display = (
        'lesson_number',
        'lesson_title',
        'masterclass'
    )

    ordering = ('lesson_number',)

admin.site.register(Artist, ArtistAdmin)
admin.site.register(MasterclassOverview)
admin.site.register(Masterclass, LessonAdmin)
