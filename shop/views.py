from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin

from .models import Shop
from .serializers import ShopSerializer


class ShopViewSet(CreateModelMixin): # POSTs

      serializer_class = ShopSerializer
      queryset = Shop.objects.all()