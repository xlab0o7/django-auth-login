from django.contrib import admin
from .models import Fooditems

#Register your models here.
# @admin.register(FoodList)
# class foodList(admin.ModelAdmin):
#     list_display = [
#         'food_items',
#         'calories'
#     ]
    
    # fields = "__all__"
    
    
    
#     model = users

@admin.register(Fooditems)
class foodAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'calories', 'ucalories', 'uname']
    # inlines = [UpdateUser]
