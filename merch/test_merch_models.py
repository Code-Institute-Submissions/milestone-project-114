from django.test import TestCase
from .models import Merch


class TestMerchModels(TestCase):

    def test_merch_item_id_defaults_to_true(self):
        item = Merch.objects.create(id=1234, price=1234)
        self.assertTrue(item.id)
