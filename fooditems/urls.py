from django.urls import path
# from .views import FoodItemsViewSet
from .views import delFoodlog, editItems, foodhome
from . import views

urlpatterns = [
    path("", foodhome.as_view(), name='foodhome'),
    path("delFoodlog/", delFoodlog.as_view(), name="delFoodlog"),
    path("addItems/", views.addItems.as_view(), name="addItems"),
    path("deleteItems/", views.deleteItems.as_view(), name="deleteItems"),
    path("editItems/<int:id>/", editItems.as_view(), name="editItems"),
]

# urlpatterns = [
#     path("", FoodItemsViewSet.as_view(), name="foodhome"),
#     path("/<int:id>/", FoodItemsViewSet.as_view(), name="fooditem-details")
# ]

# path("app2/", views.app2.as_view(), name="app2")
# path("newUser/", views.addUser.as_view(), name="addUser")

# urlpatterns = [
#     path("", FoodItemsViewSet.list),  # type: ignore
#     path("", FoodItemsViewSet.create, name="makefood"),
#     path("", FoodItemsViewSet.delete, name="fooddel"),
#     # path("/", FoodItemsViewSet)
# ]
