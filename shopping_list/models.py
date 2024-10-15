from django.db import models
import uuid

from django.db import models


# Create your models here.
    #ShoppingList model
class ShoppingList(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name= models.CharField(max_length=200)

    def __str__(self):
        return self.name

    #shoppingItems model
class ShoppingItems(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    purchased = models.BooleanField()
    shopping_list = models.ForeignKey(ShoppingList, on_delete= models.CASCADE, related_name="shopping_items")

    def __str__(self):
            return f"{self.name}",

#next command to load data
#python manage.py loaddata initial_shopping_lists_with_items.json


