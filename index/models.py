from django.db import models


class Features(models.Model):

    class Meta:
        verbose_name_plural = 'Features'

    featured_artist = models.CharField(max_length=254)
    thumbnail_url = models.CharField(max_length=512)
    post_url = models.CharField(max_length=254)

    def __str__(self):
        return self.featured_artist
