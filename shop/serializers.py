from rest_framework.serializers import ModelSerializer
from .models import Shop

class ShopSerializer(ModelSerializer):
    class Meta:
        model = Shop
        fields = (
            'id', 'name', 'address', 'rating'
        )