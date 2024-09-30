# shopping_list/api/viewsets.py

from rest_framework.viewsets import ModelViewSet
from shopping_list.api.serializer import ShoppiItemSerializer
from shopping_list.models import ShoppingItems

class ShoppingItemsViewSet (ModelViewSet):
    queryset= ShoppingItems.objects.all()
    serializer_class = ShoppiItemSerializer