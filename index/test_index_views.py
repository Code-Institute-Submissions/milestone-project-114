from django.test import TestCase


class TestIndexViews(TestCase):

    def test_get_index(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index/index.html')
