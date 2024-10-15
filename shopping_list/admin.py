from django.contrib import admin

from shopping_list.models import ShoppingItems, ShoppingList

# Register your models here.
admin.site.register(ShoppingItems)
admin.site.register(ShoppingList)