from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.views import generic
from caloriesTracker.models import ListFoodItems, DailyFoodInTake
from .form_list import AddItemsFood
from fooditems.models import Fooditems
# from django.contrib.auth.models import User

# Create your views here.


class home(generic.ListView):
    # model = Tracker
    template_name = "tracker/tracker.html"
    context_object_name = "track"

    def get_queryset(self):
        food = Fooditems.objects.all().values()
        return food

#  for other application below code

# class foodlist(generic.ListView):
#     model = Fooditems
#     template_name = "tracker/app2.html"
#     context_object_name = 'foods'

#     def get_queryset(self) -> QuerySet[Any]:
#         return Fooditems.objects.all()


def food_list(request):
    foods = ListFoodItems.objects.all()
    return render(request, "tracker/app2.html", {'foods': foods})


class addFoodItems(generic.CreateView):
    model = ListFoodItems
    template_name = "tracker/addfood_list.html"
    form_class = AddItemsFood
    success_url = '/fooditems'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def add_food(request, food_id):
    food_item = ListFoodItems.objects.get(pk=food_id)
    DailyFoodInTake.objects.create(
        user=request.user, food_items=food_item, quantity=1)
    return redirect('daily_intake')


def daily_intake(request):
    daily_intake = DailyFoodInTake.objects.filter(user=request.user)
    total_calories = sum(item.food_items.calories *
                         item.quantity for item in daily_intake)
    return render(request, 'tracker/dailyInTake.html', {'daily_intake': daily_intake, 'total_calories': total_calories})
