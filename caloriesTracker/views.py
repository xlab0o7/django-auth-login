from django.shortcuts import get_object_or_404, redirect, render
from django.views import View, generic
from caloriesTracker.models import DailyFoodTake
from fooditems.models import Fooditems

# Create your views here.


class home(generic.ListView):
    template_name = "tracker/tracker.html"
    context_object_name = "track"

    def get_queryset(self):
        food = Fooditems.objects.all().values()
        return food


class foodlist(View):
    def get(self, request):
        allfoods = Fooditems.objects.all()
        foodlist = DailyFoodTake.objects.filter(user=request.user)
        return render(request, "tracker/app2.html", {'foods': allfoods, 'listfood': foodlist})

    def post(self, request):
        selected_food = request.POST.get('selected_Food')
        list = get_object_or_404(Fooditems, id=selected_food)
        print(f'selectedfood: {selected_food} list: {list}')
        food = DailyFoodTake(user=request.user, food_items=list)
        food.save()
        return redirect('caloriesTracker:foodlist')
