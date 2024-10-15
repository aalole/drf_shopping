from rest_framework import generics

from shopping_list.api.serializer import ShoppiItemSerializer, ShoppingListSerializer 
from shopping_list.models import ShoppingList, ShoppingItems

class ListAddShoppingList(generics.ListCreateAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer


class ShoppingListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer

class AddShoppingItem(generics.CreateAPIView):
    queryset = ShoppingItems.objects.all()
    serializer_class = ShoppiItemSerializer

class ShoppingItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=ShoppingItems.objects.all()
    serializer_class = ShoppiItemSerializer
    lookup_url_kwarg= "item_pk"