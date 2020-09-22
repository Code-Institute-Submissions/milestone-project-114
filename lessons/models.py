from django.db import models


class Artist(models.Model):
    artist_name = models.CharField(max_length=254)
    artist_friendly_name = models.CharField(max_length=254)
    discipline1 = models.CharField(max_length=254)
    discipline2 = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    skill_level1 = models.CharField(max_length=254)
    skill_level2 = models.CharField(max_length=254, null=True, blank=True)
    skill_level3 = models.CharField(max_length=254, null=True, blank=True)
    artist_image = models.ImageField()

    def __str__(self):
        return self.artist_name

    def get_artist_friendly_name(self):
        return self.artist_friendly_name


class MasterclassOverview(models.Model):

    class Meta:
        verbose_name_plural = 'Masterclasses'

    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
    masterclass_title = models.CharField(max_length=254)
    masterclass_title_friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.masterclass_title


class Masterclass(models.Model):

    class Meta:
        verbose_name_plural = 'Masterclass Lessons'

    masterclass = models.ForeignKey('MasterclassOverview', related_name='lessons', on_delete=models.CASCADE)
    lesson_title = models.CharField(max_length=254)
    lesson_number = models.IntegerField()
    lesson_description = models.TextField()
    video_url = models.URLField(max_length=1024)

    def __str__(self):
        return self.lesson_title
