from django.test import TestCase
from .models import MasterclassOverview, Artist


class TestLessonsViews(TestCase):

    def test_masterclasses_view(self):
        response = self.client.get('/artist-masterclasses/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/masterclasses.html')

    def test_masterclass_view(self):
        artist = Artist.objects.create(artist_name='Test Artist Name')
        artist = Artist.objects.get(artist_name='Test Artist Name')
        masterclass = MasterclassOverview.objects.create(
            artist=artist,
            masterclass_title='Test Masterclass Title'
        )
        response = self.client.get(
            f'/artist-masterclasses/{masterclass.masterclass_title}'
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/masterclass.html')
