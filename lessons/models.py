from django.db import models
from subscriptions.models import Pricing


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
        return self.artist_friendly_name

    def get_artist_friendly_name(self):
        return self.artist_friendly_name


class MasterclassOverview(models.Model):

    class Meta:
        verbose_name_plural = 'Masterclasses'

    pricing_tiers = models.ManyToManyField(Pricing, blank=True)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
    masterclass_title = models.CharField(max_length=254)
    masterclass_title_friendly_name = models.CharField(max_length=254)

    lesson_title1 = models.CharField(max_length=254, null=True, blank=True)
    lesson_number1 = models.IntegerField(null=True, blank=True)
    lesson_description1 = models.TextField(null=True, blank=True)
    video_url1 = models.URLField(max_length=1024, null=True, blank=True)
    img_url1 = models.URLField(max_length=1024, null=True, blank=True)

    lesson_title2 = models.CharField(max_length=254, null=True, blank=True)
    lesson_number2 = models.IntegerField(null=True, blank=True)
    lesson_description2 = models.TextField(null=True, blank=True)
    video_url2 = models.URLField(max_length=1024, null=True, blank=True)
    img_url2 = models.URLField(max_length=1024, null=True, blank=True)

    lesson_title3 = models.CharField(max_length=254, null=True, blank=True)
    lesson_number3 = models.IntegerField(null=True, blank=True)
    lesson_description3 = models.TextField(null=True, blank=True)
    video_url3 = models.URLField(max_length=1024, null=True, blank=True)
    img_url3 = models.URLField(max_length=1024, null=True, blank=True)

    lesson_title4 = models.CharField(max_length=254, null=True, blank=True)
    lesson_number4 = models.IntegerField(null=True, blank=True)
    lesson_description4 = models.TextField(null=True, blank=True)
    video_url4 = models.URLField(max_length=1024, null=True, blank=True)
    img_url4 = models.URLField(max_length=1024, null=True, blank=True)

    lesson_title5 = models.CharField(max_length=254, null=True, blank=True)
    lesson_number5 = models.IntegerField(null=True, blank=True)
    lesson_description5 = models.TextField(null=True, blank=True)
    video_url5 = models.URLField(max_length=1024, null=True, blank=True)
    img_url5 = models.URLField(max_length=1024, null=True, blank=True)

    lesson_title6 = models.CharField(max_length=254, null=True, blank=True)
    lesson_number6 = models.IntegerField(null=True, blank=True)
    lesson_description6 = models.TextField(null=True, blank=True)
    video_url6 = models.URLField(max_length=1024, null=True, blank=True)
    img_url6 = models.URLField(max_length=1024, null=True, blank=True)

    lesson_title7 = models.CharField(max_length=254, null=True, blank=True)
    lesson_number7 = models.IntegerField(null=True, blank=True)
    lesson_description7 = models.TextField(null=True, blank=True)
    video_url7 = models.URLField(max_length=1024, null=True, blank=True)
    img_url7 = models.URLField(max_length=1024, null=True, blank=True)

    lesson_title8 = models.CharField(max_length=254, null=True, blank=True)
    lesson_number8 = models.IntegerField(null=True, blank=True)
    lesson_description8 = models.TextField(null=True, blank=True)
    video_url8 = models.URLField(max_length=1024, null=True, blank=True)
    img_url8 = models.URLField(max_length=1024, null=True, blank=True)

    lesson_title9 = models.CharField(max_length=254, null=True, blank=True)
    lesson_number9 = models.IntegerField(null=True, blank=True)
    lesson_description9 = models.TextField(null=True, blank=True)
    video_url9 = models.URLField(max_length=1024, null=True, blank=True)
    img_url9 = models.URLField(max_length=1024, null=True, blank=True)

    lesson_title10 = models.CharField(max_length=254, null=True, blank=True)
    lesson_number10 = models.IntegerField(null=True, blank=True)
    lesson_description10 = models.TextField(null=True, blank=True)
    video_url10 = models.URLField(max_length=1024, null=True, blank=True)
    img_url10 = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.masterclass_title
