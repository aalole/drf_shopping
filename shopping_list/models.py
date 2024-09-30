from django.db import models
import uuid

from django.db import models


# Create your models here.
class ShoppingItems(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    purchased = models.BooleanField()

    def __str__(self):
        return f"{self.name}"