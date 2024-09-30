# shopping_list/urls.py

from django.urls import path, include
from rest_framework import routers

from shopping_list.api.viewset import ShoppingItemsViewSet

router = routers.DefaultRouter()
router.register("shopping-items", ShoppingItemsViewSet, basename='shopping-items')

urlpatterns = [
    path("api/", include(router.urls)),
]