from django.test import TestCase
from.models import Shop
from ..serializers import ShopSerializer
from django.urls import reverse
from rest_framework import status


"""
Test performed maps to function in models.py file.
"""

class TestShopModel(TestCase):
    def test_shop_as_a_string(self):
        # Test name given to oject equal to the item as a string
        item = Shop(name="Create a Test")
        self.assertEqual("Create a Test", str(item))
        
"""
Test performed to function in serializers.py file.Test
"""

class TestShopSerializer(TestCase):
    def test_model_fields(self):
        """Serializer data matches the Company object for each field."""
        shop = Shop()
        for field_name in [
            'id', 'name', 'address', 'rating'
        ]:
            self.assertEqual(
                'serializer.data'[field_name],
                getattr(shop, field_name)
            )

"""
Test performed on POST function.
"""

def test_post(self):
          """POST to create a Shop."""
          data = {
              'name': 'New name',
              'address': 'New address',
              'rating': 'New rating',
          }
          self.assertEqual(Shop.objects.count(), 0)
          response = self.client.post(self.list_url, data=data)
          self.assertEqual(response.status_code, status.HTTP_201_CREATED)
          self.assertEqual(Shop.objects.count(), 1)
          shop = Shop.objects.all().first()
          for field_name in data.keys():
                self.assertEqual(getattr(shop, field_name), data[field_name])