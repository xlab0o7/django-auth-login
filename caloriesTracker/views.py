from django.views import generic
from fooditems.models import Fooditems
from django.contrib.auth.models import User

# Create your views here.

class home(generic.ListView):
    # model = Tracker
    template_name = "tracker/tracker.html"
    context_object_name = "track"
    
    def get_queryset(self):
        food = Fooditems.objects.all().values()
        return food
        # user = User.objects.values_list("username", flat=True)
        # return {"food":food,"users":user}
    
    # def calories_validation(self, calories, total_calories, tolerance_percentage):
    #     difference = abs(calories - total_calories)
    #     tolerance = total_calories * tolerance_percentage / 100

    #     if difference <= tolerance:
    #         return True
    #     else:
    #         return False

    
    # def my_view(self, request):
    #     calories = request.POST.get('calories')
    #     total_calories = request.POST.get('total_calories')
    #     tolerance_percentage = 5  # Adjust the tolerance percentage as needed

    #     if not self.calories_validation(calories, total_calories, tolerance_percentage):
    #         error_message = 'Calories value is too close to total calories'
    #         return render(request, 'template.html', {'error_message': error_message})  
    
    #     track = self.get_queryset()
    #     return render(request, self.template_name, {'track': track})
    
    
