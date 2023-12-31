from django.db import models
from django.contrib.auth.models import User
from fooditems.models import Fooditems

# Create your models here.


class ListFoodItems(models.Model):
    names = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()
    List = models.ForeignKey(Fooditems, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.names


class DailyFoodTake(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_items = models.ForeignKey(Fooditems, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.food_items.name
