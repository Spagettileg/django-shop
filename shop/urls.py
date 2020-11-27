from django.conf.urls import include, re_path
from rest_framework.routers import DefaultRouter
from .views import ShopViewSet


router = DefaultRouter()
router.register(['shop'], ShopViewSet, base_name='shop')

urlpatterns = [
    re_path('^', include(router.urls)),
]