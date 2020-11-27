from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin

from .models import Shop
from .serializers import ShopSerializer

"""
queryset created to pave the way for read, update and delete requests.
"""

class ShopViewSet(CreateModelMixin): # POSTs

      serializer_class = ShopSerializer
      queryset = Shop.objects.all()