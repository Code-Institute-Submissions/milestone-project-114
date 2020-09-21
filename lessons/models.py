from django.db import models


class Artist(models.Model):
    artist_name = models.CharField(max_length=254)
    discipline1 = models.CharField(max_length=254)
    discipline2 = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    skill_level1 = models.CharField(max_length=254)
    skill_level2 = models.CharField(max_length=254, null=True, blank=True)
    skill_level3 = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.artist_name

class MasterclassOverview(models.Model):
    artist_name = models.ForeignKey('Artist', null=True, blank=True, on_delete=models.SET_NULL)
    masterclass_title = models.CharField(max_length=254)

    def __str__(self):
        return self.artist

class Masterclass(models.Model):
    masterclass_title = models.ForeignKey('MasterclassOverview', null=True, blank=True, on_delete=models.SET_NULL)
    lesson_title = models.CharField(max_length=254)
    lesson_description = models.TextField()
    video_url = models.URLField(max_length=1024)

    def __str__(self):
        return self.masterclass_title
