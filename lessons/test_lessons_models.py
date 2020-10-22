from django.test import TestCase
from .models import Artist, MasterclassOverview


class TestLessonsModels(TestCase):

    def test_artist_id_defaults_to_true(self):
        artist = Artist.objects.create(artist_name='Test Artist Name')
        self.assertTrue(artist.id)

    def test_masterclass_id_defaults_to_true(self):
        artist = Artist.objects.create(artist_name='Test Artist Name')
        artist = Artist.objects.get(artist_name='Test Artist Name')
        masterclass = MasterclassOverview.objects.create(
            artist=artist
        )
        self.assertTrue(masterclass.id)
