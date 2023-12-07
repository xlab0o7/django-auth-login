from django.urls import path
from .views import editItems
from . import views

urlpatterns = [
    path("", views.foodhome.as_view(), name='foodhome'),
    path("addItems/", views.addItems.as_view(), name="addItems"),
    path("deleteItems/", views.deleteItems.as_view(), name="deleteItems"),
    path("editItems/<int:id>/", editItems.as_view(), name="editItems"),
    # path("newUser/", views.addUser.as_view(), name="addUser")
]