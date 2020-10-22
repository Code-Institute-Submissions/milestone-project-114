from django.test import TestCase
from .models import Merch


class TestMerchViews(TestCase):

    def test_store_view(self):
        response = self.client.get('/store/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'merch/store.html')

    def test_item_detail_view(self):
        item = Merch.objects.create(id=1234, price=1234, image='1234.jpeg')
        response = self.client.get(f'/store/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'merch/item_detail.html')
