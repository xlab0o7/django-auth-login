from django.urls import path
from . import views
# from .views import food_list, add_food, daily_intake

app_name = "caloriesTracker"

urlpatterns = [
    path("", views.home.as_view(), name="home1"),
    path("list/", views.foodlist.as_view(), name="foodlist"),
]
# path("addFoodItems/", views.addFoodItems.as_view(), name="addFoodItems"),
# path("food_list/", food_list, name="food_list"),
# path("add_food/<int:food_id>/", add_food, name="add_food"),
# path("daily_intake/", daily_intake, name="daily_intake")
