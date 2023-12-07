from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.
# class FoodList(models.Model):
#     food_items = models.CharField(max_length=100)
#     calories = models.IntegerField()
    
#     def __str__(self) -> str:
#         return self.food_items
       
class Fooditems(models.Model):
    # FoodKey = models.ForeignKey(FoodList, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    calories = models.IntegerField(default=250)
    ucalories = models.IntegerField()
    uname = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.uname:
            self.uname = get_user_model().objects.get(username=self.user.username).username # type: ignore

        super().save(*args, **kwargs)
        
    # def display_users(self):
    #     return ", " .join(str(p) for p in self.user.first_name )
