# shopping_list/api/serializers.py

from rest_framework import serializers
from shopping_list.models import ShoppingItems

class ShoppiItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingItems
        fields = ["id", "name", "purchased"]
        read_only_fields = ("id",)