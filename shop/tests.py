from django.test import TestCase
from.models import Shop
from ..serializers import ShopSerializer

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